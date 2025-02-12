from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder("This is a DataMatrix.")
encoder.save("sample_barcodes/datamatrix_test.png")
print(encoder.get_ascii())
