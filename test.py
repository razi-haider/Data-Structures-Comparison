from timeit import default_timer as timer
import sys
import random
sys.path.append("./src")
from AVL import AVLTree
from SkipList import SkipList
from BST import Node
import zipfile
import io

'''
Doing experiments in here. Ignore this file.

'''


# lines = []
# for i in range(10000000):
#     lines.append(str(random.randint(1000, 99999999999)))
# with open('integers_dataset.txt', 'w') as d:
#     for line in lines:
#         d.write(line)
#         d.write('\n')
# d.close()





# lines = random.sample(range(99999999999), 10000000)
# with open('integers_dataset_test.txt', 'w') as d:
#     for line in lines:
#         d.write(str(line))
#         d.write('\n')
# d.close()

# dataset_numbers = []
# with open('integers_dataset.txt', 'r') as f:
#     for line in f:
#         dataset_numbers.append(int(line.strip()))
# f.close()


# def operations_AVL(data:list):

#     myTree = AVLTree()
#     root = [None, None, None, None, None, None]
#     to_return = {}
#     print("AVL_Insert")
#     for k in range(5):
#         start = timer()
#         for i in range(10*10**(k+1)):
#             root[k] = myTree.insert_node(root[k], data[i])
#         end = timer()
#         print('For', 10*10**(k+1),':', end - start)
#         to_return['AVL_Insert_' + str(10*10**(k+1))] = end - start

#     return to_return





# # newlist = [] # empty list to hold unique elements from the list
# # duplist = [] # empty list to hold the duplicate elements from the list
# # for i in dataset_numbers:
# #     if i not in newlist:
# #         newlist.append(i)
# #     else:
# #         duplist.append(i) # this method catches the first duplicate entries, and appends them to the list
# # # The next step is to print the duplicate entries, and the unique entries
# # print("List of duplicates", duplist)

# lines = []

# myunique = set(dataset_words) # prints the final list without any duplicates
# newlines = []
# for i in myunique:
#     newlines.append(i)

# with open('words_dataset_test.txt', 'w') as d:
#     for line in newlines:
#         d.write(line)
#         d.write('\n')
# d.close()





# def words():
#     results_BST = []
#     results_AVL = []
#     results_SkipList = []
#     final_lst = [] #list of tuples
#     num_tries = 2


#     for x in range(num_tries):
#         results_BST.append(operations_BST(dataset_words))
#         results_AVL.append(operations_AVL(dataset_words))
#         results_SkipList.append(operations_SkipList(dataset_words))

#     #take average of all the values in the list

#     for key in results_BST[0]:
#         temp = []
#         for i in range(num_tries):
#             temp.append(results_BST[i][key])
        
#         final_lst.append((key, sum(temp)/len(temp)))
    
#     for key in results_AVL[0]:
#         temp = []
#         for i in range(num_tries):
#             temp.append(results_AVL[i][key])
        
#         final_lst.append((key, sum(temp)/len(temp)))

#     for key in results_SkipList[0]:
#         temp = []
#         for i in range(num_tries):
#             temp.append(results_SkipList[i][key])
        
#         final_lst.append((key, sum(temp)/len(temp)))



#     print(final_lst)









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

    

# x = operations_BST(dataset_words)