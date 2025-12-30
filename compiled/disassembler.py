import dis
import example1, example2, example3, example4

PYC_CODE_MODULES = [
    example1, 
    example2, 
    example3, 
    example4
]


DISEMBLED_CODE_FILES = [
    "example1.txt",
    "example2.txt",
    "example3.txt",
    "example4.txt"
]

if __name__ == "__main__":
    for output_file, module in zip(DISEMBLED_CODE_FILES, PYC_CODE_MODULES):
        with open(output_file, 'w', encoding='utf-8') as dis_file:
            dis.dis(module, file=dis_file)

        print(f'Код {module} дизассемблирован и сохранен в {output_file}')




