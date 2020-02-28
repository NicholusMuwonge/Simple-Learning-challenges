"""

An array with an odd number of elements is said to be centered if all elements (except the middle one) are strictly greater than the value of the middle element. Note that only arrays with an odd number of elements have a middle element. Write a function that accepts an integer array and returns 1 if it is a centered array, otherwise it returns 0.
Examples:

if the input array is	return
{1, 2, 3, 4, 5}	0 (the middle element 3 is not strictly less than all other elements)
{3, 2, 1, 4, 5}	1 (the middle element 1 is strictly less than all other elements)
{3, 2, 1, 4, 1}	0 (the middle element 1 is not strictly less than all other elements)
{1, 2, 3, 4}	0 (no middle element)
{}	0 (no middle element)
{10}	1 (the middle element 10 is strictly less than all other elements)
 
"""

def Check_Odds(array):
  # Find the middle element in an array
  print_out=0
  length_array=len(array)
  if length_array%2!=0:
    middle_key=array[int(length_array/2)]
  # check size of the rest of the keys
    if min(array)!=middle_key:
      print_out=0
    elif len(array)==0 or len(array)%2==0:
      print_out*=0
    else:
      print_out=1
  print(print_out)

array=[1,2,2,0,0,4,4,5]
Check_Odds(array)
min(array)


