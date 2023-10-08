from ..Controller.CreateNote import CreateNote

print('+---------------------------------------------+')
print('|----------- Bem vindo ao Simnote! -----------|')
print('|---------------------------------------------|')
print('| O que deseja fazer hoje?                    |')
print('| (1) Criar uma nota                          |')
print('| (2) Editar uma nota                         |')
option = int(input('| '))

if option == 1:
    print('| Digite o titulo da sua nota                 |')
    note_title = input('| ')
    print('| Digite sua nota:                            |')
    note_content = input('| ')

    CreateNote(note_title, note_content)
    print('| Nota criada com sucesso!                    |')