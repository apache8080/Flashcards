#!/usr/local/bin/python
#Author: Rishi Desai
#Flashcard app

from random import randint

set = ()

def add_term(term, definition):
    global set
    set_list=list(set)
    item = {'Term':term, 'Definition': definition}
    set_list.append(item)
    set = tuple(set_list)
    return item

def remove_term(term):
    global set
    set_list=list(set)
    for i in set_list:
        if i['Term']==term:
            set_list.remove(i)
            set = tuple(set_list)
            break

def list_terms():
    global set
    for i in set:
        print i

def find_term(term):
    global set
    typ = type(term)
    if typ == int:
        return set[term-1]
    elif typ == str:
        for i in set:
            if i['Term']==term:
                return i
def is_correct(ans, term):
    if ans == term:
        print "Correct"
        return True
    else:
        return False
    
def quiz_set():
    print "Welcome to quiz mode"
    print "The definition will be given for a random term and you need to answer the right term "
    global set
    set_list = list(set)
    correct=0
    rand_index=-1
    while len(set_list)>1:
        #print len(set_list)
        rand_index=randint(0,len(set_list)-1)
        term = set_list[rand_index]
        print "definition: "+str(term['Definition'])
        ans = raw_input("answer:")
        if is_correct(ans, term['Term']):
            correct+=1
        else:
            print "Wrong"
            print "correct answer: "+term['Term']
        set_list.remove(term)
        #print set_list
    term = set_list[0]
    print "definition: "+str(term['Definition'])
    ans = raw_input("answer:")
    if is_correct(ans, term['Term']):
        correct+=1
    else:
        print "Wrong"
        print "correct answer: "+term['Term']
    
    percent_correct= float(correct)/float(len(set))
    print "Quiz Complete!"
    print "Your Stats:"
    print "Number Right: "+ str(correct)
    print "Number Wrong: "+ str(len(set)-correct)
    print "Percent Correct: "+str(percent_correct*100.0)+"%"

def save_set(set_name, new):
    global set
    file_name = set_name+'.txt'
    if new == 1:
        with open('set_name.txt', 'ab') as set_file:
            set_file.write(set_name+'\n')
    file = open(file_name, 'w')
    for i in set:
        set_term = i['Term']+','+i['Definition']
        file.write(set_term+'\n')

def load_set(set_name):
    global set
    set = ()
    file_name = set_name+'.txt'
    file = open(file_name, 'r')
    for line in file:
        term_list = line.split(',')
        add_term(term_list[0],term_list[1].strip('\n'))

def update_set(add_or_remove,set_name, term, definition):
    file_name = set_name+'.txt'
    if add_or_remove == 0:
        with open(file_name,'ab') as file:
            set_term = term+','+definition
            file.write(set_term+'\n')
    elif add_or_remove == 1:
        save_set(set_name, 0)

def list_sets():
    file = open('set_name.txt', 'r')
    for line in file:
        print line
        
def main():
    global set
    create_or_load=-1
    print "Welcome to Rishi's Flashcards!"
    print "Enter 1 to create a new set"
    print "Enter 2 to load a created set"
    #print "Previously Created Sets"
    list_sets()
    create_or_load = int(raw_input("Answer: "))
    load_set_name = ''

    if create_or_load == 2:
        load_set_name= raw_input('Enter the set\'s name: ')
        load_set(load_set_name)
        list_terms()

    while True:
        print "Input Options:"
        print "  -Enter 1 to add a term to the set"
        print "  -Enter 2 remove a term to the set"
        print "  -Enter 3 to print the entire set"
        print "  -Enter 4 to search for a term in the set"
        print "  -Enter 5 to do the quiz"
        if create_or_load == 1:
            print "  -Enter 6 to save the set"
        print "  -Enter 0 to exit the program"
        ans = int(raw_input("Answer: "))
        if ans ==0:
            print "Goodbye"
            break
        elif ans == 1:
            print (chr(27)+"[2J")
            term = raw_input("Enter the term:")
            definition = raw_input("Enter the definition of the term:")
            if create_or_load == 1:
                print "Term Added: Term: "+str(add_term(term, definition))
            elif create_or_load == 2:
                update_set(0,load_set_name, term, definition)
                print "Term Added: Term: "+str(add_term(term, definition))
            print ""
            print ""
            print ""
        elif ans == 2:
            print (chr(27)+"[2J")
            list_terms()
            term = raw_input("Enter the term:")
            remove_term(term)
            if create_or_load == 2:
                update_set(1,load_set_name, '', '')
            list_terms()
            print ""
            print ""
            print ""
        elif ans == 3:
            print (chr(27)+"[2J")
            list_terms()
            print ""
            print ""
            print ""
        elif ans == 4:
            print (chr(27)+"[2J")
            list_terms()
            print "there are "+str(len(set))+" in this set"
            print "Enter 1 to search by term"
            print "Enter 2 to search by term number"
            typ = int(raw_input())
            if typ == 1:
                term = raw_input("Enter the term:")
            else:
                term = int(raw_input("Enter the term number:"))
            print "Searched Term:"
            print find_term(term)
            print ""
            print ""
            print ""
        elif ans == 5:
            print (chr(27)+"[2J")
            quiz_set()
            print ""
            print ""
            print ""
        elif ans == 6:
            print (chr(27)+"[2J")
            if create_or_load == 1:
                set_name = raw_input('Enter the set name: ')
                save_set(set_name, 1)
            
if __name__ == '__main__':
    main()
