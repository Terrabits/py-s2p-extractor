from rohdeschwarz.instruments.vna import Vna

def query_64_bit_complex(self, scpi):
    self.settings.binary_64_bit_data_format = True
    self.write(scpi)
    return self.read_64_bit_complex_vector_block_data()
Vna.query_64_bit_complex = query_64_bit_complex
