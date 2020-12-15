{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><a name=\"sections\"></a></p>\n",
    "\n",
    "\n",
    "# Sections\n",
    "\n",
    "- <a href=\"#fileIO\">File Input and Output</a>\n",
    " - <a href=\"#read\">Reading from Files</a>\n",
    " - <a href=\"#output\">File Output</a>\n",
    "- <a href=\"#DS\">Data Structures</a>\n",
    " - <a href=\"#mutate\">Mutating Operations on Lists</a>\n",
    " - <a href=\"#TSD\">Tuple, sets and Dictionaries</a>\n",
    "- <a href=\"#conditionals\">Conditionals</a>\n",
    "- <a href=\"#for\">For Loop</a>\n",
    "- <a href=\"#while\">While Loop</a>\n",
    "- <a href=\"#error\">Errors and Exceptions</a>\n",
    " - <a href=\"#built\">Built-in Exceptions</a>\n",
    " - <a href=\"#handle\">Handling Exceptions</a>\n",
    "- <a href=\"#sol\">Solutions</a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><a name=\"fileIO\"></a></p>\n",
    "\n",
    "# File Input and Output\n",
    "\n",
    "Follow the steps below to create a .txt file in iPython notebook:\n",
    "\n",
    "- Save your notebook and go to the initial iPython screen.\n",
    "- In the New menu (upper right), click Text File.\n",
    "- Enter at least two lines of text.\n",
    "- Click on “untitled.txt” in the top left to name the file.\n",
    "- Enter the name \"simple.txt\".\n",
    "- Select “Save” from the file menu to save it.\n",
    "- Click the word Jupyter on top left to return to the iPython screen. You should see your new file listed.\n",
    "\n",
    "\n",
    "<p><a name=\"read\"></a></p>\n",
    "\n",
    "## Reading from Files\n",
    "\n",
    "- Before inputing the file, it is a good practice to inspect the file first. One could go back to the initial iPython screen to look at the file. \n",
    "- With iPython notebook, a file can be inspected without leaving the working space. \n",
    "- This may be accomplished using command line instructions after the `!` symbol.\n",
    "\n",
    "**Note**: this is not python code, but a special feature in iPython notebook."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is a new file\r\n",
      "this is this line 2"
     ]
    }
   ],
   "source": [
    "!cat simple.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Windows users use `type` command."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "simple.txt not found\r\n"
     ]
    }
   ],
   "source": [
    "!type simple.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Reading from files is very simple, because we can treat a file almost as a list of strings.\n",
    "\n",
    "- To turn a file into a list of strings, simply call the `readlines` function.\n",
    "- The first three lines of code read the file into a list of strings.\n",
    "- Note that the lines of the txt file are seperated by a newline `\\n`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open('simple.txt', 'r')    # 'r' for read\n",
    "lines = f.readlines()\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['This is a new file\\n', 'this is this line 2']"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lines"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that we have the file in a list, we can apply all of our list and string processing powers to it.  E.g. turn all letters in simple.txt into uppercase:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "THIS IS A NEW FILE\n",
      "THIS IS THIS LINE 2\n"
     ]
    }
   ],
   "source": [
    "text = ''.join(list(map(lambda s: s.upper(), lines)))\n",
    "print(text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 1** \n",
    "\n",
    "File input\n",
    "\n",
    "- The `‘\\n’` symbol in the previous example is quite annoying. Try to get rid of it using the `strip()` function.\n",
    "- Write a function `e_to_a` to read the contents of a file, and get a list of every line, with the letter `‘e’` changed to `‘a’` in every line.\n",
    "```\n",
    "e_to_a('simple.txt') ---> [\"I'm lina 1,\", \"and I'm lina 2.\"]\n",
    "```\n",
    "Hint: Start with the usual code to read the lines of the file, then map replace over the lines and return the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "### Your code here\n",
    "# 1\n",
    "list(map(lambda s: s.strip('\\n'), lines))\n",
    "\n",
    "# 2\n",
    "def e_to_a(filename):\n",
    "    f = open(filename, 'r')\n",
    "    lines_  = f.readlines()\n",
    "    \n",
    "    list(map(lambda s:s.replace('e', 'a'), lines_))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><a name=\"output\"></a></p>\n",
    "\n",
    "## File Output\n",
    "\n",
    "Writing output to a file is easy.\n",
    "\n",
    "- Open file for output:  `f = open(filename, 'w')`. \n",
    "**Caution**: Once this line of code is executed, the file specified by the filename would be **ERASED!!**\n",
    "- Write a string, `s`,  to the file:  `f.write(s)`\n",
    "- Close the file:  `f.close()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is a new file\r\n",
      "this is this line 2"
     ]
    }
   ],
   "source": [
    "!cat simple.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open('simple.txt', 'w')\n",
    "f.write('This overwrites the file!')\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- If you see an error, try using `f = open('simple.txt', 'wb')`\n",
    "- It will write the file in the binary mode, which is more universal.\n",
    "- When you read the file back, you need to call `f = open('simple.txt', 'rb')`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This overwrites the file!"
     ]
    }
   ],
   "source": [
    "!cat simple.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you want to append a string to the end of the file, we may open the file for appending:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open('simple.txt', 'a') # 'a' for appending\n",
    "f.write('\\nThis should be the second line.')\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "# with open(\"simple.txt\", \"r\") as f:\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This overwrites the file!\r\n",
      "This should be the second line."
     ]
    }
   ],
   "source": [
    "!cat simple.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can open a file for both reading and writing at the same time:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['This overwrites the file!\\n', 'This should be the second line.']"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f = open('simple.txt', 'r+')\n",
    "lines = f.readlines()\n",
    "lines"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We may then write a new line into it:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "f.write('\\nThis should be the third line.')\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This overwrites the file!\r\n",
      "This should be the second line.\r\n",
      "This should be the third line."
     ]
    }
   ],
   "source": [
    "!cat simple.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- It is a good practice to use the **with** keyword when dealing with file objects. Pay attention to the indentation.\n",
    "- This has the advantage that the file is properly closed after it suites finishes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('simple.txt', 'r+') as f:\n",
    "    lines = f.readlines()\n",
    "    f.write('\\nWe are using with keyword this time.')\n",
    "    f.write('\\nNo need to close the file.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This overwrites the file!\r\n",
      "This should be the second line.\r\n",
      "This should be the third line.\r\n",
      "We are using with keyword this time.\r\n",
      "No need to close the file."
     ]
    }
   ],
   "source": [
    "!cat simple.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><a name=\"DS\"></a></p>\n",
    "\n",
    "# Data Structures\n",
    "\n",
    "While lists are the most widely used data structure in Python, they are not the only one. Other built-in data structures are sets and dictionaries:\n",
    "- Sets - unordered collections without duplicates.\n",
    "- Dictionaries - maps from one value (often strings) to another.\n",
    "\n",
    "An important feature of Python data structures is that some are mutable and some are immutable; mutation and mutability are key concepts discussed in this section.  \n",
    "\n",
    "For example, slicing is non-mutating.  Slicing a list does not change/mutate the list itself.  See the following:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['b', 'c']"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L = ['a', 'b', 'c']\n",
    "L[1:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Slicing is non-mutating.  While `L[1:]` returns a sub-list, the original list **`L`** remains unchanged/unmutated:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'c']"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`map` and `upper` are also non-mutating functions.  Generally a function that returns a value is non-mutating."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['A', 'B', 'C']"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(map(lambda s: s.upper(), L))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`L` remains unchanged."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'c']"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><a name=\"mutate\"></a></p>\n",
    "\n",
    "## Mutating Operations on Lists"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "List is a mutable data type. The most important mutating operation is: **assignment**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "skills = ['Python','SAS','Hadoop']\n",
    "skills[1] = 'R'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Assignment does not have any output, but the value of `skills` is changed!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Python', 'R', 'Hadoop']"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "skills"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Python', 'R', 'Hadoop']"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "skills = ['Python','SAS','Hadoop']\n",
    "my_skills = skills\n",
    "skills[1] = 'R'     # no assignment to my_skills\n",
    "my_skills"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have always added a list to another list by using `+`, which is non-mutating:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'c', 'd']"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L = ['a', 'b', 'c']\n",
    "L + ['d']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "But `L` is not updated:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'c']"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Assigning the value back to `L` updates it:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'c', 'd']"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L = L + ['d']   \n",
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The `append` operation mutates a list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'c', 'd', 'e']"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L.append('e')\n",
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The `extend` operation is similar to `append` if the input is one single value. However, it will flatten the input list and then append it to the original list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "L.append([1,2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['b', 1], ['d', 3], ['a', 4], ['c', 7], [1, 2, 3]]"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "L.extend([1,2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['b', 1], ['d', 3], ['a', 4], ['c', 7], [1, 2, 3], 1, 2, 3]"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`lis.insert(i, x)` inserts `x` so that it is at location `i` in the list.  (If `i` is out of bounds, it inserts it in the closest place it can.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'd', 'c']"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L = ['a', 'b', 'c']\n",
    "L.insert(2, 'd')\n",
    "L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'd', 'c', 'e']"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L.insert(10, 'e')\n",
    "L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['f', 'a', 'b', 'd', 'c', 'e']"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L.insert(-10, 'f')\n",
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have already seen `sorted(lis)`, which is a non-mutating sort operation:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 4, 6]"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lis = [4, 2, 6, 1]\n",
    "sorted(lis)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 2, 6, 1]"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`lis.sort()` is a mutating sort operation:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "lis.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 4, 6]"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A mutating operation applied to `lis` changes the value of another variable pointing to the same memory location as `lis`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 4, 6]"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lis = [4, 2, 6, 1]\n",
    "lis2 = lis\n",
    "lis.sort()\n",
    "lis2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using `sorted(lis)` doesn't cause the change on `lis2`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 4, 6]"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lis = [4, 2, 6, 1]\n",
    "lis2 = lis\n",
    "sorted(lis)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 2, 6, 1]"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lis2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- The change in a variable that shares a memory location as another is called a side effect of the mutating operation.\n",
    "- Programmers try to avoid side effects, because it is difficult to understand code when variables can change without even being mentioned.\n",
    "- Note that the mutating operations seen have no return value, or rather, their return value is `None`.  Try:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(lis.sort())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Application of mutating operations in a map will not return the desired map.  This is an attempt to extend every element of a nested list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[None, None, None]"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# this will not retrun the desired map\n",
    "L = [[1], [2], [3]]\n",
    "list(map(lambda l: l.append(4), L))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, 4], [2, 4], [3, 4]]"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# but it will apply the mutating operation to every element in the list\n",
    "L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For a nested list, `sort` and `sorted` use the first element as the primary sort key, the second element as the second sort key, etc., and they sort in ascending order. You can customize the sort using user-defined key:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['Lucy', 'A', 9], ['Peter', 'A', 6], ['John', 'B', 3]]"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "staff =[['Lucy','A',9], ['John','B',3], ['Peter','A',6]]\n",
    "sorted(staff, key = lambda x: x[1]) # key is the sort metric"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['John', 'B', 3], ['Peter', 'A', 6], ['Lucy', 'A', 9]]"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "staff =[['Lucy','A',9], ['John','B',3], ['Peter','A',6]]\n",
    "sorted(staff, key = lambda x: x[2]+len(x[0]))  # key is the sort metric"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- You can define functions that use mutating operations. If the purpose of a function is to perform a mutating operation, it does not need a return value.\n",
    "\n",
    "- This function sorts a nested list, using the given element of each sublist as the sort key:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [],
   "source": [
    "def sort_on_field(lis, fld):\n",
    "    lis.sort(key = lambda x: x[fld])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "L = [['a', 4], ['b', 1], ['c', 7], ['d', 3]]\n",
    "sort_on_field(L, 1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It has no return, and does not produce a value. But it mutates the variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['b', 1], ['d', 3], ['a', 4], ['c', 7]]"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 2**\n",
    "\n",
    "Write a function to switch the ith and jth items in a list.\n",
    "```\n",
    "def switch_item(L, i, j):\n",
    "    ... function body goes here ...\n",
    "\n",
    "my_list = ['first', 'second', 'third', 'fourth']\n",
    "switch_item(my_list, 1, -1)\n",
    "my_list ---> ['first', 'fourth', 'third', 'second']\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-64-6ab6dc68cf16>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-64-6ab6dc68cf16>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    def switch_item(L, i, j):\u001b[0m\n\u001b[0m                             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "#### Your code here\n",
    "def switch_item(L, i, j):\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "# old way\n",
    "# a = 1\n",
    "# b = 2\n",
    "# temp = a\n",
    "# a = b\n",
    "# b = temp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "# new way switching items\n",
    "# a, b = b, a\n",
    "\n",
    "# a, b, c = *[blah]\n",
    "\n",
    "lst = [1, 2, 3]\n",
    "a, b, c = lst\n",
    "print(a)\n",
    "print(b)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "lst1 = [1,2,3]\n",
    "lst2 = lst1.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 'b', 3]\n",
      "[1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "lst1[1] = 'b'\n",
    "\n",
    "print(lst1)\n",
    "print(lst2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "<p><a name=\"TSD\"></a></p>\n",
    "\n",
    "## Tuples, sets and dictionaries\n",
    "\n",
    "We can now explain the other data types of Python.\n",
    "- **Strings**:  Like lists of characters.  Immutable.\n",
    "- **Tuples**:  Tuples are like lists, but are immutable.\n",
    "- **Sets**:  Also like lists, except that they do not have duplicate elements.  Mutable.\n",
    "- **Dictionaries**:  These are tables that associate values with keys (usually strings).  Mutable.\n",
    "\n",
    "\n",
    "**Strings**\n",
    "\n",
    "Strings are immutable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'str' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-65-24fd28dc6477>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mcompany\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'NYC DataScience Academy'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mcompany\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'A'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: 'str' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "company = 'NYC DataScience Academy'\n",
    "company[0] = 'A'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'AYC DataScience Academy'"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'A'+company[1:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "**Tuples**\n",
    "\n",
    "- Tuples are similar to lists, but they are immutable.\n",
    "- Tuples are written with parentheses instead of square brackets."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-67-56957a2dbf17>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mcourses\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;34m'Programming'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'Stats'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'Math'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mcourses\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'Algorithms'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "courses = ('Programming', 'Stats', 'Math') \n",
    "courses[2] = 'Algorithms'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Tuples support all the non-mutating list operations:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('Stats', 'Math')"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "courses[1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Programming', 'Stats', 'Math']"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(map(lambda s: s.capitalize(), courses))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Tuples and lists both allow a shorthand for assignment that allows all the elements of the tuple or list to be assigned to variables at once:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(a,b) = (1,2)   # works with lists also\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This provides a handy way to swap variables:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(a,b) = (b,a)\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Function can return multiple values at the same time. \n",
    "- Make sure you have the exact same number of variables when you assign the output of your function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "def square_all(x, y):\n",
    "    return x**2, y**2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [],
   "source": [
    "x, y = square_all(2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4, 9)"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x, y"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you have more variables to assign than the output, you will get an error like the following. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "not enough values to unpack (expected 3, got 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-123-34df216529e9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mz\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msquare_all\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m: not enough values to unpack (expected 3, got 2)"
     ]
    }
   ],
   "source": [
    "x, y, z = square_all(2,3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Extra Bonus"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def what_happens(x):\n",
    "    x = x+1\n",
    "    return (x)\n",
    "\n",
    "y = 2\n",
    "what_happens(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y = what_happens(y)\n",
    "y"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Set**\n",
    "\n",
    "- A set is an unordered collection with no duplicate elements.  Sets are mutable.\n",
    "\n",
    "- To create a set, you can use either curly braces or the `set()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'a', 'e', 'i', 'o', 'u'}"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vowels = {'u','a','e','i','o','u','i'}\n",
    "vowels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'apple', 'orange', 'pear'}"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit = set(['apple', 'orange', 'apple', 'pear'])\n",
    "fruit"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Sets support non-mutating list operations, as long as they don’t depend on order:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'set' object is not subscriptable",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-130-fd8aef860b34>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mprimes\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m5\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m7\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mprimes\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: 'set' object is not subscriptable"
     ]
    }
   ],
   "source": [
    "primes = {2, 3, 5, 7}\n",
    "primes[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "17"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(primes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{4, 9, 25, 49}"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(map(lambda x: x*x, primes))       # order is not guaranteed"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`set` is a mutable data type, but **all the elements need to be immutable data type**, i.e. you can't add a list to a set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unhashable type: 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-133-a0b90856e768>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mprimes\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madd\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m8\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;31m# add() is how you update an existing set\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: unhashable type: 'list'"
     ]
    }
   ],
   "source": [
    "primes.add([4,6,8]) # add() is how you update an existing set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2, 3, 4, 5, 7}"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "primes.add(4)\n",
    "primes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n",
      "-1049109503896013892\n",
      "7135221661056972208\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "unhashable type: 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-136-70e66d3d2434>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhash\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'9'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhash\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m11\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m13\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m17\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhash\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m8\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: unhashable type: 'list'"
     ]
    }
   ],
   "source": [
    "print(hash(2))\n",
    "print(hash(3))\n",
    "print(hash('9'))\n",
    "print(hash((11,13,17)))\n",
    "print(hash([4,6,8]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{(11, 13, 17), 2, 3, 4, 5, 7, '9'}"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "primes.add('9')\n",
    "primes.add((11,13,17))\n",
    "primes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Again, order is not guaranteed for a set object. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{-2, -6, 1, 210, 'a'}"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x=[1,-2,-6,210, 'a']\n",
    "set(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sets have mathematical operations like union (|), intersection (&), difference (-), and symmetric difference (^)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = {'a', 'b', 'c'}\n",
    "b = {'b', 'c', 'd'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'a', 'b', 'c', 'd'}"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a | b       # union"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'b', 'c'}"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a & b       # intersection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'a'}"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a - b       # difference"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'a', 'd'}"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a ^ b       # symmetric difference (a-b | b-a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Dictionaries**\n",
    "\n",
    "- A dictionary is a set of keys with associated values. Each key can have just one value associated with it.  Dictionaries are mutable.\n",
    " - Any immutable object can be a key, including numbers, strings, and tuples of numbers or strings.  Strings are the most common.\n",
    " - Any object can be a value.\n",
    "\n",
    "- Dictionaries are written in curly braces (like sets), with the key/value pairs separated by colons:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# coding challenge\n",
    "# if you were given two strings, how would you find the unique account of those to strings\n",
    "# 'panama' and 'banana'\n",
    "# a = 3\n",
    "# one becomes a key and the other value\n",
    "# iterate through and add on \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'sex': 'male', 'height': 6.1, 'age': 30}"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "employee = {'sex': 'male', 'height': 6.1, 'age': 30}\n",
    "employee"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The most important operation on dictionaries is key lookup:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "employee['age']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can add new key: value pairs to the dictionary:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'sex': 'male', 'height': 6.1, 'age': 30, 'city': 'New York'}"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "employee['city'] = 'New York'\n",
    "employee"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is illegal to access a key that is not present:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'weight'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-147-b338b7fb4410>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0memployee\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'weight'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m: 'weight'"
     ]
    }
   ],
   "source": [
    "employee['weight']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "but you can check if a key is present using the in operator:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'weight' in employee"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Dictionary has a function called `get()`, which will return the corresponding value of the given key if it exists in the dictionary, return the value you passed to the function otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "150"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "employee.get('weight', 150)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "However, the dictionary itself stays the same."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'sex': 'male', 'height': 6.1, 'age': 30}"
      ]
     },
     "execution_count": 157,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "employee"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can also get a list of the keys, the values, or all key/value pairs:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['sex', 'height', 'age'])"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "employee = {'sex': 'male', 'height': 6.1, 'age': 30}\n",
    "employee.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values(['male', 6.1, 30])"
      ]
     },
     "execution_count": 159,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "employee.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([('sex', 'male'), ('height', 6.1), ('age', 30)])"
      ]
     },
     "execution_count": 160,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "employee.items()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For convenience, you can construct a dictionary from a list (or set) of tuples:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'sape': 4139, 'guido': 4127, 'jack': 4098}"
      ]
     },
     "execution_count": 161,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 3**\n",
    "\n",
    "- Given the following dictionary:\n",
    "```\n",
    "inventory = {'pumpkin': 20, 'fruit': ['apple', 'pear'], 'vegetable': ['potato','onion','lettuce']}\n",
    "```\n",
    "- Modify inventory as follows:\n",
    " - Add a meat inventory item containing 'beef', 'chicken', and 'pork'.\n",
    " - Sort the vegetables (Recall the sorted function.)\n",
    " - Add five more pumpkins.\n",
    "After these changes, inventory is:\n",
    "```\n",
    "{'vegetable': ['lettuce', 'onion', 'potato'], 'fruit': ['apple', 'pear'],\n",
    " 'meat': ['beef', 'chicken', 'pork'], 'pumpkin': 25}\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [],
   "source": [
    "inventory = {'pumpkin' : 20, 'fruit' : ['apple', 'pear'],\n",
    "           'vegetable' : ['potato','onion','lettuce']}\n",
    "\n",
    "#### Your code here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Python has some other useful data types in the collections module.\n",
    "- Two most commonly used data types are [Counter](https://docs.python.org/3/library/collections.html#collections.Counter) and [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter, defaultdict"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><a name=\"conditionals\"></a></p>\n",
    "\n",
    "# Conditionals\n",
    "\n",
    "- We have seen boolean functions in the `filter` operator. Booleans can also be used inside functions, to do different calculations depending upon properties of the input.\n",
    "\n",
    "- For example, recall the function firstelt.  It returns the first element of a list:\n",
    "```\n",
    "def firstelt(L):\n",
    "    return L[0]\n",
    "```\n",
    "- It throws an error if its argument is the empty list. The function could be more robust if it returns **None** when passed the empty list.  \n",
    "- **None** is a special value in Python used for these types of cases."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {},
   "outputs": [],
   "source": [
    "def firstelt(L):\n",
    "    if L == []:\n",
    "        return None\n",
    "    else:\n",
    "        return L[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "L1=[]\n",
    "L2=[1,2,3]\n",
    "print(firstelt(L1))\n",
    "print(firstelt(L2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- The syntax for a conditional in a function is:\n",
    "```\n",
    "if condition:                # any boolean expression\n",
    "    return expression        # return is indented from if\n",
    "else:                        # else starts in same column as if\n",
    "    return expression        # return is indented from else\n",
    "```\n",
    "- The syntax in `lambda` definitions is different:\n",
    "```\n",
    "lambda x: expression if condition else expression\n",
    "```\n",
    "\n",
    "- For example, here is `firstelt` in lambda syntax:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [],
   "source": [
    "Firstelt = lambda L: None if L==[] else L[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Conditionals can be nested arbitrarily:\n",
    "- Return A if c1 is true, B if c1 is false but c2 is true, and C if both are false:\n",
    "```python\n",
    "if c1:\n",
    "    return A\n",
    "else:\n",
    "    if c2:\n",
    "        return B\n",
    "    else:\n",
    "        return C\n",
    "```\n",
    "- Having an `if` follow an `else` is so common there is special syntax for it:\n",
    "```python\n",
    "if c1:\n",
    "    return A\n",
    "elif c2:\n",
    "    return B\n",
    "else:\n",
    "    return C\n",
    "```\n",
    "- Return A if c1 and c2 are true, B if c1 is true but not c2, C if c1 is false but c3 is true, and D if c1 and c3 are both false:\n",
    "```python\n",
    "if c1:\n",
    "    if c2:\n",
    "        return A\n",
    "    else:\n",
    "        return B\n",
    "elif c3:\n",
    "    return C\n",
    "else:\n",
    "    return D\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 4**\n",
    "\n",
    "Define the following functions using if conditionals:\n",
    " 1. `choose(response, choice1, choice2)` returns `choice1` if `response` is the string `'y'` or `'yes'`, and `choice2` otherwise.\n",
    " 2. `leap_year(y)` returns true if `y` is divisible by 4, except if it is divisible by 100; but it is still true if `y` is divisible by 400. Thus, 1940 is a leap year, 1900 isn’t, and 2000 is.\n",
    " 3. Use `filter` to define a function `leap_years` that selects from a list of numbers those that represent leap years."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#### Your code here\n",
    "\n",
    "#1\n",
    "\n",
    "\n",
    "#2\n",
    "\n",
    "\n",
    "#3\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><a name=\"for\"></a></p>\n",
    "\n",
    "# For loop\n",
    "\n",
    "A simple example is printing the elements of a list. Since `print()` function does not return any value, we can’t use it in `map()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "words = ['a', 'b', 'c', 'd', 'e']\n",
    "for word in words:\n",
    "    print(word)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "for i in \"anything\":\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Recall that the range function generates a list of numbers:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "for i in range(len(words)):\n",
    "    print(i, words[i])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The Python function `enumerate()` returns both the index and element as a tuple from the list, simultaneously."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "words = ['a', 'b', 'c', 'd', 'e']\n",
    "for i, e in enumerate(words):\n",
    "    print(i, e)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- In addition to the iteration variable taking on values in a list, you may want other variables to take on different values in each iteration.  You can accomplish this by “self-assigning” to those variables.  \n",
    "- The following loop sums the elements of a list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "primes = [2, 3, 5, 7, 11]\n",
    "sum_ = 0    # Do not overwrite the built-in sum() function\n",
    "for p in primes:\n",
    "    sum_ = sum_ + p\n",
    "sum_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- We have already learned how to write string to a file when we were talking about file I/O. However, sometimes you need to write multiple lines of string to a file instead of just one.\n",
    "\n",
    "- Recall this is the syntax for writing a string s to file.\n",
    "\n",
    " - Open file for output:  `f = open(filename, 'w')`\n",
    "\n",
    " - Write a string to the file:  `f.write(s)`\n",
    "\n",
    " - Close the file:  `f.close()`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A loop can be used to iterate through a list containing all the strings, writing each string to the file.\n",
    "Suppose we want to write the following output to a file, instead of printing it out."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "words = ['a', 'b', 'c', 'd', 'e']\n",
    "for i, e in enumerate(words):\n",
    "    print(i, e)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Will it work if `f.write(i, e)` is called in the for loop?\n",
    "\n",
    "- In this example, i is an integer and e is a string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "with open('loop.txt', 'w') as f:\n",
    "    for i, e in enumerate(words):\n",
    "        s = str(i) + e\n",
    "        f.write(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "!cat loop.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "But seems like it is not exactly the same as we want. We need to append a newline character at the end of string."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 5**\n",
    "\n",
    "- For this exercise, we want to write the key and value pairs from the following dictionary to a file called **dictionary.txt**:\n",
    "\n",
    "```\n",
    "inventory = {'pumpkin' : 3.99, 'potato': 2, \n",
    "             'apple' : 2.99}\n",
    "potato 2\n",
    "apple 2.99\n",
    "pumpkin 3.99\n",
    "```\n",
    "\n",
    "- Use .items() to get the key and value pair of a dictionary.\n",
    "- The values of the dictionary are of different types, you can use str() function to convert either a float or integer to a string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#### Your code here\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><a name=\"listComp\"></a></p>\n",
    "\n",
    "# List Comprehension\n",
    "\n",
    "- List comprehensions are another notation for defining lists. They mimic the mathematical notation of “set comprehensions” and have a concise syntax.  In one step, list comprehensions can perform the combined operation of any filter and map.\n",
    "- A list comprehension has the form: \n",
    "```\n",
    "[ <expresion> for <element> in <list> if <boolean> ]\n",
    "```\n",
    "\n",
    "- First consider the list comprehension that squares every element in a list, as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "[ x* x for x in [1, 2, 3, 4, 5]] #pure map"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note the above list comprehension has no `if` statement.  The following list comprehension includes an if statement.  This comprehension squares every even element in a list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "[ x* x for x in [1, 2, 3, 4, 5] if x%2==0] #map and filter"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- A list comprehension can also use if/else statements.  These types of list comprehensions have a slightly different syntax.\n",
    "\n",
    "- A list comprehension with an if/else statements has the form: \n",
    "```\n",
    "[ <expr1> if <boolean> else <expr2> for <element> in <list> ]\n",
    "```\n",
    "- Consider the list comprehension that squares even element in a list and adds two to every odd element, as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "[ x* x if x%2==0 else x+2 for x in [1, 2, 3, 4, 5] ]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This final example extracts the first element of every non-empty sublist."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "[l[0] for l in nested_list1 if l != []]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you have difficulties understanding list comprehensions, think about it like a for loop. \n",
    "\n",
    "```python\n",
    "for item in list:\n",
    "    if conditional:\n",
    "        expression\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 6**\n",
    "\n",
    "Write list comprehensions to create the following lists:\n",
    " - The square roots of the numbers in `[1, 4, 9, 16]`. (Recall that `math.sqrt` is the square root function.)\n",
    " - The even numbers in a numeric list `L`. Define several lists `L` to test your list comprehension. \n",
    " **Hint** (`n` is even if and only if `n % 2 == 0`.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#### Your code here\n",
    "\n",
    "#1\n",
    "\n",
    "\n",
    "#2\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><a name=\"while\"></a></p>\n",
    "\n",
    "# While Loop\n",
    "\n",
    "- While loops are used when the condition for terminating the loop is known, but not necessarily the number of iterations.  Examples include:\n",
    " - Summing the elements of a list up to the first zero.\n",
    " - Using Newton’s method to find the argument of a function that makes it zero valued.  This works by finding values which make the function approach zero.  The iterations stop when the method converges, finding an argument which brings the value within a certain range of zero.\n",
    " - Getting input from a user until the user enters ‘quit’.\n",
    " \n",
    "- When using a while loop, iteration continues until a given condition becomes false:\n",
    "```\n",
    "while <condition>:\n",
    "   statements\n",
    "```\n",
    "- As a first example, this loop prints integers from 0 to 9:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "i = 0\n",
    "while i < 10:\n",
    "    print(i)\n",
    "    i = i + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This for loop does the same thing:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "for i in range(0, 10):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- One thing we can do with while loops that is hard to do with for loops is to terminate early.  \n",
    "- This loops adds up integers starting from 1 until the sum exceeds n:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "n = 20\n",
    "i = 1\n",
    "sum_ = 0 # Do not overwrite the built-in sum() function\n",
    "while sum_ <= n:\n",
    "    sum_ = sum_ + i\n",
    "    i = i + 1\n",
    "sum_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This loop is similar, but sums the numbers in a list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "L = [5, 10, 15, 20, 25]\n",
    "\n",
    "n = 20\n",
    "i = 0\n",
    "sum_ = 0\n",
    "while sum_ <= n:\n",
    "    sum_ = sum_ + L[i]\n",
    "    i = i + 1\n",
    "    \n",
    "sum_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "When iterating over a list like this, care must be taken not to go out of bounds. Without doing so, we might end up with the following:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "n = 80\n",
    "i = 0\n",
    "sum_ = 0\n",
    "while sum_ <= n:\n",
    "    sum_ = sum_ + L[i]\n",
    "    i = i + 1\n",
    "sum_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This problem can be fixed by modifying the header:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "n = 80\n",
    "i = 0\n",
    "sum_ = 0\n",
    "while sum_ <= n and i < len(L):\n",
    "    sum_ = sum_ + L[i]\n",
    "    i = i + 1\n",
    "    \n",
    "sum_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Break** and **Continue** Statements\n",
    "\n",
    "- The **break** statement immediately terminates the (for or while) loop it is in.  This provides a way to terminate the loop within the middle of the body. \n",
    "\n",
    "- The **continue** statement terminates the current iteration of the loop and goes back to the header.\n",
    "\n",
    "- The loop below adds the values in a list, but ignores negative numbers, and stops if the number exceeds 100:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "L = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60]\n",
    "\n",
    "sum_ = 0\n",
    "for x in L:\n",
    "    if x < 0:\n",
    "        continue\n",
    "    sum_ = sum_ + x\n",
    "    if sum_ > 100:\n",
    "        break\n",
    "        \n",
    "sum_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 7**\n",
    "\n",
    "Calculate the sum of integers that can be divided by 7 and less than 100. In the following example code, we use while True, which means the while loop will keep running until you break it.\n",
    "\n",
    "```\n",
    "i = 0\n",
    "sum_ = 0\n",
    "while True:\n",
    "\n",
    "\t# Type your code here\n",
    "\n",
    "print sum_\n",
    "```\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "i = 0\n",
    "sum_ = 0\n",
    "while True:\n",
    "    # Type your code here\n",
    "\n",
    "print(sum_)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><a name=\"error\"></a></p>\n",
    "\n",
    "# Errors and Exception Handling\n",
    "\n",
    "- Exceptions and errors are messages given by Python indicating there is a problem in the interpretation or running of a program.  \n",
    "- Without exception handling these errors will cause the program to stop.  \n",
    "\n",
    "- Typical errors/exceptions arise from:\n",
    " - Opening a file that does not exist\n",
    " - Dividing by zero\n",
    " - Adding two incompatible objects\n",
    " - Using a poorly formatted string\n",
    " - A bad function argument\n",
    "\n",
    "- Consider the exceptions raised from the following examples of code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "f=open('nonexistent.txt','r')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "1/0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "'one'+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "\"hello'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "int('hi')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "'hello'[10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note the different exceptions raised in the examples above:\n",
    "\n",
    "- FileNotFoundError: a file or folder referenced can't be found\n",
    "- ZeroDivisionError: division by zero\n",
    "- TypeError: incorrect object type used in a statement\n",
    "- SyntaxError: statement syntax incorrectly structured\n",
    "- ValueError: incorrect value used in a statement\n",
    "- IndexError: index referenced does not exist  \n",
    "\n",
    "The complete list is here: https://docs.python.org/3.6/library/exceptions.html"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**raise** statement\n",
    "\n",
    "Exceptions/errors may also by raised manually using **raise** followed by an exception type with an optional message string. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "raise TypeError('Houston we have a problem')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The use of **raise** allows the coder to determine additional circumstances when an error/exception will arise.  The generic exception type `Exception` is useful for this."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "raise Exception(\"Do not do that\")\n",
    "print('will this print?')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Note in the example above the print function following the exception does not execute.  This is because exceptions will terminate the running of a program unless they are handled.\n",
    "\n",
    "- In practice raising exceptions is often used in the body of a function: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def cal_volume(x,y,z):\n",
    "    if x <= 0 or y <= 0 or z <= 0:\n",
    "        raise ValueError('The value of each dimension should be greater than 0!')\n",
    "    else:\n",
    "        return x*y*z"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "cal_volume(-2, 3, 4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exception Handling\n",
    "\n",
    "- The exception handling mechanism allows a program to deal with exceptions/errors gracefully, without terminating the program.\n",
    "\n",
    "- The mechanism has two parts:  \n",
    " - **try** executing some code which may potentially raise an exception\n",
    " - **except** catching the exception and responding appropriately\n",
    "\n",
    "```\n",
    "try:\n",
    "        commands\n",
    "except Exception:\n",
    "        handle exception\n",
    "```\n",
    "\n",
    "- Many predefined functions, or functions imported from modules, will raise exceptions.  For example, the function open below raises an error when a file indicated by filename does not exist.\n",
    "\n",
    "- The following exception handling will keep the program from terminating and simply print an error message:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def openfile(filename, mode):\n",
    "    try:\n",
    "        f = open(filename, mode)\n",
    "    except:\n",
    "        print('Error:', filename, 'does not exist')\n",
    "        \n",
    "        \n",
    "openfile('nonexistent.txt', 'r')\n",
    "print('moving on')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><a name=\"built\"></a></p>\n",
    "\n",
    "## Specific Exception Handling\n",
    "\n",
    "- The previous except clause - with no specific exception named - catches all exceptions. However, it is best to be specific about what exceptions you want to catch, so that you won’t respond inappropriately. \n",
    "\n",
    "- For example, the problem of the code below is that we specify a mode that does not exist, but the error message we print out is not true -- `loop.txt` does exist."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def openfile(filename, mode):\n",
    "    try:\n",
    "        f = open(filename, mode)\n",
    "    except:\n",
    "        print('Error:', filename, 'does not exist')\n",
    "        \n",
    "openfile('loop.txt', 'no_such_mode')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "!cat loop.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In order to communicate the specific eror to the user the specific error may be routed to the print function using the **except** Exception **as** syntax, as shown:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def openfile(filename, mode):\n",
    "    try:\n",
    "        f = open(filename, mode)\n",
    "    except Exception as e:\n",
    "        print(type(e),e)\n",
    "        \n",
    "openfile('nonexistent.txt', 'r')\n",
    "openfile('loop.txt', 'no_such_mode')\n",
    "openfile('loop.txt', 123)\n",
    "print('life goes on')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- To deal with specific errors, use multiple exceptions.\n",
    "\n",
    "- The general form of the try statement, and the meaning of the various parts, is as follows:\n",
    "\n",
    "```\n",
    "try:\n",
    "    statements\t\t\t# start by executing these\n",
    "except name:\n",
    "    statements\t\t\t# execute if exception “name” was raised\n",
    "...\n",
    "except:\n",
    "    statements\t\t\t# execute if an exception was raised that is not named above\n",
    "else:\n",
    "    statements\t\t\t# execute if no exception was raised\n",
    "finally:\n",
    "    statements\t\t\t# execute no matter what\n",
    "```\n",
    "\n",
    "For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def openfile(filename, mode):\n",
    "    try:\n",
    "        f = open(filename, mode)\n",
    "    except FileNotFoundError:\n",
    "        print('File doesn\\'t exist in this case.')\n",
    "    except ValueError:\n",
    "        print('Likely to be wrong mode in this case.')\n",
    "    except TypeError:\n",
    "        print('Mode has to be a string.')\n",
    "    else:\n",
    "        print('No error')\n",
    "    finally:\n",
    "        print('Everybody should have this!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Test the code below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "print(\"openfile('nonexistent.txt', 'r')\")\n",
    "print('-'*50)\n",
    "openfile('nonexistent.txt', 'r')\n",
    "print('\\n')\n",
    "\n",
    "print(\"openfile('loop.txt', 'no_such_mode')\")\n",
    "print('-'*50)\n",
    "openfile('loop.txt', 'no_such_mode')\n",
    "print('\\n')\n",
    "\n",
    "print(\"openfile('loop.txt', 123)\")\n",
    "print('-'*50)\n",
    "openfile('loop.txt', 123)\n",
    "print('\\n')\n",
    "\n",
    "print( \"openfile('loop.txt', 'r')\")\n",
    "print('-'*50)\n",
    "openfile('loop.txt', 'r')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "<p><a name=\"sol\"></a></p>\n",
    "\n",
    "# Solutions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 1**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "lines = list(map(lambda s: s.strip(), lines))\n",
    "\n",
    "def e_to_a(filename):\n",
    "    f = open(filename, 'r')\n",
    "    lines = f.readlines()\n",
    "    lines = list(map(lambda word: word.strip().replace('e', 'a'), lines))\n",
    "    f.close()\n",
    "    return lines\n",
    "\n",
    "e_to_a('simple.txt')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 2**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def switch_item(L, i, j):\n",
    "    temp = L[i]\n",
    "    L[i] = L[j]\n",
    "    L[j] = temp"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 3**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "inventory = {'pumpkin' : 20, 'fruit' : ['apple', 'pear'],\n",
    "           'vegetable' : ['potato','onion','lettuce']}\n",
    "inventory['meat']=['beef', 'chicken', 'pork']\n",
    "inventory['vegetable'] = sorted(inventory['vegetable'])\n",
    "inventory['pumpkin'] = inventory['pumpkin'] + 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "**Exercise 4**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#1\n",
    "def choose(response, choice1, choice2):\n",
    "    if response == 'y' or response == 'yes':\n",
    "        return choice1\n",
    "    else:\n",
    "        return choice2\n",
    "\n",
    "#2\n",
    "def leap_year(y):\n",
    "    return y % 400 == 0 or (y % 4 ==0 and y % 100 != 0)\n",
    "\n",
    "#3\n",
    "leap_years = lambda L:  filter(leap_year, L)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 5**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "f = open('dictionary.txt', 'w')\n",
    "inventory = {'pumpkin' : 3.99, 'potato': 2, \n",
    "             'apple' : 2.99}\n",
    "for i, j in inventory.items():\n",
    "    string = i + ' ' + str(j) + '\\n'\n",
    "    f.write(string)\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 6**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#1\n",
    "import math\n",
    "[math.sqrt(x) for x in [1, 4, 9, 16]]\n",
    "\n",
    "#2\n",
    "[x for x in L if x % 2 == 0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise 7**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "i = 0\n",
    "sum_ = 0\n",
    "while True:\n",
    "    if i > 100:\n",
    "        break\n",
    "    if i % 7 == 0:\n",
    "        sum_ += i\n",
    "    i += 1\n",
    "\n",
    "print sum_"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}