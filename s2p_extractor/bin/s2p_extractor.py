#!/usr/bin/env python
import argparse
from   rohdeschwarz                 import print_header
from   rohdeschwarz.instruments.vna import Vna
from   s2p_extractor                import calculate
from   s2p_extractor.corrections    import Corrections
from   s2p_extractor.source         import Source, Type
import sys

def main():
    parser = argparse.ArgumentParser(description='Connect to a Rohde & Schwarz VNA')
    parser.add_argument('--visa', metavar='bus', default=False,
                        help="use VISA with 'bus'")
    parser.add_argument('--address', default='127.0.0.1',
                        help='instrument address')
    parser.add_argument('--port',    default=5025, type=int,
                        help='port (TCP only)')
    parser.add_argument('--timeout', default=5000, type=int,
                        help='default instrument timeout (ms)')
    parser.add_argument('--log',
                        help='SCPI command log filename')
    parser.add_argument('--export-cal-data', action='store_true',
                        help='Save corrections to numpy `savez` (*.pyz) data file')
    parser.add_argument('--outer-channel', type=int,
                        help='channel with outer corrections')
    parser.add_argument('--outer-cal-group',
                        help='cal group containing outer corrections')
    parser.add_argument('--inner-channel', type=int,
                        help='channel with inner corrections')
    parser.add_argument('--inner-cal-group',
                        help='cal group containing inner corrections')
    parser.add_argument('--filename', default='Port {port}.s2p',
                        help="default: 'Port {port}.s2p'")
    parser.add_argument('ports', type=int, nargs='+',
                        help='VNA ports to extract DUTs from')
    args = parser.parse_args()

    if not args.inner_channel and not args.inner_cal_group:
        print('error: must include inner source, either channel or cal group')
        parser.print_help()
        sys.exit(-1)
    if not args.outer_channel and not args.outer_cal_group:
        print('error: must include outer source, either channel or cal group')
        parser.print_help()
        sys.exit(-1)

    vna = Vna()
    try:
        if args.visa:
            vna.open(args.visa, args.address)
        else:
            vna.open_tcp(args.address, args.port)
        if args.timeout:
            vna.timeout_ms = args.timeout

        if vna.connected():
            if args.log:
                vna.open_log(args.log)
                print_header(vna.log, 'R&S S2P Extractor', '1.0')
                vna.print_info()
        else:
            raise Exception('Could not connect to instrument')

        if args.outer_channel:
            outer_source = Source(Type.CHANNEL,   args.outer_channel)
        else:
            outer_source = Source(Type.CAL_GROUP, args.outer_cal_group)
        if args.inner_channel:
            inner_source = Source(Type.CHANNEL,   args.inner_channel)
        else:
            inner_source = Source(Type.CAL_GROUP, args.inner_cal_group)
        print(f"ports: {args.ports}")
        for port in args.ports:
            filename = args.filename.format(port=port)
            print(f'  {filename}')
            calculate(vna, outer_source, inner_source, port, filename, args.export_cal_data)
    except Exception as err:
        parser.print_help()
        raise
    finally:
        if vna.connected():
            vna.errors
            vna.clear_status()
        if vna.log:
            vna.close_log()
        if vna.connected():
            vna.close()

if __name__ == '__main__':
    main()
    sys.exit(0)
