import boto3
from botocore.exceptions import NoCredentialsError

class FakeS3:
    def __init__(self):
        self.buckets =  {}

    def create_bucket(self, bucket_name):
        """Simula a criação de um bucket S3"""
        if bucket_name not in self.buckets:
            self.buckets[bucket_name] = []
            print(f"Bucket '{bucket_name}' criado com sucesso.")
        else:
            print(f"Bucket '{bucket_name}' já existe.")

    def upload_file(self, bucket_name, file_name, content):
        """Simula o upload de um arquivo para o bucket"""
        if bucket_name in self.buckets:
            self.buckets[bucket_name].append({'file_name': file_name, 'content': content})
            print(f"Arquivo '{file_name}' carregado no bucket '{bucket_name}'.")
        else:
            print(f"Erro: O bucket '{bucket_name}' não existe.")

    def list_files(self, bucket_name):
        """Simula a listagem de arquivos dentro do bucket"""
        if bucket_name in self.buckets:
            print(f"Arquivos no bucket '{bucket_name}':")
            for file in self.buckets[bucket_name]:
                print(f" - {file['file_name']}")
        else:
            print(f"Erro: O bucket '{bucket_name}' não existe.")


# Simulação de uso
s3 = FakeS3()

# Criando buckets
s3.create_bucket('meu-bucket')
s3.create_bucket('outro-bucket')

# Fazendo upload de arquivos
s3.upload_file('meu-bucket', 'file1.txt', 'Conteúdo do arquivo 1')
s3.upload_file('meu-bucket', 'file2.txt', 'Conteúdo do arquivo 2')

# Listando arquivos do bucket
s3.list_files('meu-bucket')

# Tentando fazer upload em um bucket não existente
s3.upload_file('bucket-inexistente', 'file3.txt', 'Conteúdo do arquivo 3')
