from timeit import default_timer as timer
import zipfile, io, sys, random, csv
sys.path.append("./src")
from AVL import AVLTree
from SkipList import SkipList
from BST import Node



def main():
    dataset_words = []
    dataset_numbers = []



    with zipfile.ZipFile("Datasets.zip") as zf: #open the zip file
        with io.TextIOWrapper(zf.open("words_dataset.txt"), encoding="utf-8") as f: #open the file inside the zip file
            for line in f:
                dataset_words.append(line.strip()) #strip the newline character and add to list
            f.close() #close the file


    with zipfile.ZipFile("Datasets.zip") as zf:
        with io.TextIOWrapper(zf.open("integers_dataset.txt"), encoding="utf-8") as f:
            for line in f:
                dataset_numbers.append(int(line))
            f.close()
    

    results_words = operations(dataset_words)
    results_numbers = operations(dataset_numbers)

    with open('results_words.csv', mode='w') as csv_file: #open the csv file
        headers = ['Operation', 'Time Taken']
        results_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) #create the writer object
        results_writer.writerow(headers) #write the headers

        for item in results_words: #for each tuple in the final list
            results_writer.writerow([item[0], item[1]]) #write the tuple to the csv file
        
    csv_file.close()

    with open('results_numbers.csv', mode='w') as csv_file: #open the csv file
        headers = ['Operation', 'Time Taken']
        results_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) #create the writer object
        results_writer.writerow(headers) #write the headers

        for item in results_numbers: #for each tuple in the final list
            results_writer.writerow([item[0], item[1]]) #write the tuple to the csv file
        
    csv_file.close()

    


def operations(dataset):
    results_BST = []
    results_AVL = []
    results_SkipList = []
    final_lst = [] #list of tuples
    num_tries = 11

    for x in range(num_tries):
        results_BST.append(operations_BST(dataset))
        results_AVL.append(operations_AVL(dataset))
        results_SkipList.append(operations_SkipList(dataset))


    #take average of all the values in the list of dictionaries
    for key in results_BST[0]: #for each key in the first dictionary
        temp = []
        for i in range(num_tries):  #for each dictionary in the list
            temp.append(results_BST[i][key]) #append the value of the key to a temporary list
        
        final_lst.append((key, sum(temp)/len(temp))) #append the key and the average of the values to the final list
    
    for key in results_AVL[0]:
        temp = []
        for i in range(num_tries):
            temp.append(results_AVL[i][key])
        
        final_lst.append((key, sum(temp)/len(temp)))

    for key in results_SkipList[0]:
        temp = []
        for i in range(num_tries):
            temp.append(results_SkipList[i][key])
        
        final_lst.append((key, sum(temp)/len(temp)))

    return final_lst



def operations_BST(data:list):

    TreeLst = [Node(),Node(),Node(),Node(),Node()] #list of trees  
    to_return = {}


    print("BST_Insert")
    for k in range(5): 
        myTree = TreeLst[k] #tree of kth iteration

        start = timer()
        for i in range(10*10**(k+1)):
            myTree.insert(data[i])
        end = timer()

        print('For', 10*10**(k+1),':', end - start)
        to_return['BST_Insert_' + str(10*10**(k+1))] = end - start


    print("BST_Search")
    for k in range(5):
        
        myTree = TreeLst[k]
        x = random.choice(data[:10**(k+1)])

        start = timer()
        for i in range(10**(k+1)):
            myTree.find(x)
        end = timer()

        print('For', 10**(k+1),':', end - start)
        to_return['BST_Search_' + str(10**(k+1))] = end - start


    print("BST_Delete")
    for k in range(5):
        myTree = TreeLst[k]
        x = random.choice(data[:10**(k+1)])

        start = timer()
        for i in range(10**(k+1)):
            myTree.delete(x)
        end = timer()

        print('For', 10**(k+1),':', end - start)
        to_return['BST_Delete_' + str(10**(k+1))] = end - start

    return to_return

def operations_AVL(data:list): 

    myTree = AVLTree()
    root = [None, None, None, None, None, None]
    to_return = {}


    print("AVL_Insert")
    for k in range(5):

        start = timer()
        for i in range(10*10**(k+1)):
            root[k] = myTree.insert_node(root[k], data[i])
        end = timer()

        print('For', 10*10**(k+1),':', end - start)
        to_return['AVL_Insert_' + str(10*10**(k+1))] = end - start


    print("AVL_Search")
    for k in range(5):
        x = random.choice(data[:10**(k+1)])

        start = timer()
        for i in range(10**(k+1)):
            myTree.search(root[k], x)
        end = timer()

        print('For', 10**(k+1),':', end - start)
        to_return['AVL_Search_' + str(10**(k+1))] = end - start


    print("AVL_Delete")
    for k in range(5):
        x = random.choice(data[:10**(k+1)])

        start = timer()
        for i in range(10**(k+1)):
            root[k] = myTree.delete_node(root[k], x)
        end = timer()

        print('For', 10**(k+1),':', end - start)
        to_return['AVL_Delete_' + str(10**(k+1))] = end - start


    return to_return

def operations_SkipList(data:list): 

    SkipListLst = [SkipList(),SkipList(),SkipList(),SkipList(),SkipList()]
    to_return = {}

    print("Skiplist_Insert")
    for k in range(5):
        myList = SkipListLst[k]

        start = timer()
        for i in range(10*10**(k+1)):
            myList.insert(data[i])
        end = timer()

        print('For', 10*10**(k+1),':', end - start)
        to_return['SkipList_Insert_' + str(10*10**(k+1))] = end - start

    print("Skiplist_Search")
    for k in range(5):
        myList = SkipListLst[k]
        choice = random.choice(data[:10**(k+1)])
        
        start = timer()
        for i in range(10**(k+1)):
            myList.find(choice)
        end = timer()

        print('For', 10**(k+1),':', end - start)
        to_return['SkipList_Search_' + str(10**(k+1))] = end - start

    print("Skiplist_Remove")
    for k in range(5):
        myList = SkipListLst[k]
        choice = random.choice(data[:10**(k+1)])

        start = timer()
        for i in range(10**(k+1)):
            myList.remove(choice)
        end = timer()

        print('For', 10**(k+1),':', end - start)
        to_return['SkipList_Remove_' + str(10**(k+1))] = end - start

    
    

    return to_return


main()




