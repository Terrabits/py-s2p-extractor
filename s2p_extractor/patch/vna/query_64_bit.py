from rohdeschwarz.instruments.vna import Vna

def query_64_bit(self, scpi):
    self.settings.binary_64_bit_data_format = True
    self.write(scpi)
    return self.read_64_bit_vector_block_data()
Vna.query_64_bit = query_64_bit
