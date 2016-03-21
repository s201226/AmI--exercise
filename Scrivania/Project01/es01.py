from sys import argv

end_program=0
azione=0

txt=open(argv[1])
to_do=txt.read()
txt.close()
to_do=to_do.split('\n')
for parole in to_do:
    if parole=='':
        to_do.remove('')
while end_program==0:
    print "Scegli una delle seguenti opzioni:"
    print "1- inserisci un'opzione da aggiungere alla lista"
    print "2- inserisci un'azione da rimuovere dalla lista"
    print "3- visualizza la lista"
    print "4-  chiudi il programma"

    aggiunta=""
    azione=int(raw_input())
    if azione==1:
        aggiunta=raw_input()
        to_do.append(aggiunta)
    elif azione==2:
        aggiunta=raw_input()
        to_do.remove(aggiunta)
    elif azione==3:
        print to_do
    else:
        txt=open(argv[1],"w")
        txt.truncate()
        for banane in to_do:
            txt.write(banane+'\n')
        txt.close()
        end_program=1


