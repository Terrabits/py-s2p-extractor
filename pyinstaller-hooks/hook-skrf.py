from   pathlib import Path
import skrf    as     rf


# paths
skrf_path = Path(rf.__file__).parent
snp_files = str(skrf_path / 'data' / '*.s?p')

# define datas
datas     = [(snp_files, 'skrf/data')]
