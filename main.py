{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Vh8EJWV50SeT"
   },
   "outputs": [],
   "source": [
    "class Ticket:\n",
    "\n",
    "    def setChildTicketPrice(self,child):\n",
    "        self.child = child\n",
    "\n",
    "    def getChildTicketPrice(self):\n",
    "        return self.child\n",
    "\n",
    "    def setAdultTicketPrice(self,adult ):\n",
    "        self.adult = adult\n",
    "\n",
    "    def getAdultTicketPrice(self):\n",
    "        return self.adult\n",
    "\n",
    "    def setSeniorTicketPrice(self, senior):\n",
    "        self.senior = senior\n",
    "\n",
    "    def getSeniorTicketPrice(self):\n",
    "        return self.senior\n",
    "\n",
    "  \n",
    "    def setTotal(self,total):\n",
    "        self.total = total\n",
    "\n",
    "\n",
    "    def getTotal(self):\n",
    "        return self.total"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "1JY8f_yu0gR-"
   },
   "outputs": [],
   "source": [
    "import re\n",
    "class Checkout:\n",
    "\n",
    "    def setCardNumber(self,cardno):\n",
    "        self.cardno = cardno\n",
    "\n",
    "    def getCardNumber(self):\n",
    "        return self.cardno\n",
    "\n",
    "    def setName(self,name):\n",
    "        self.name = name\n",
    "\n",
    "    def getName(self):\n",
    "        return self.name\n",
    "\n",
    "    def setExpirydate(self,expirydate):\n",
    "        self.expirydate = expirydate\n",
    "\n",
    "    def getExpirydate(self):\n",
    "        return self.expirydate\n",
    "\n",
    "    def setCVV(self,cvv):\n",
    "        self.cvv = cvv\n",
    "\n",
    "    def getCVV(self):\n",
    "        return self.cvv "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "8xd6rapE0lA-"
   },
   "outputs": [],
   "source": [
    "#Main Function\n",
    "child = []\n",
    "adult = []\n",
    "senior = []\n",
    "totalCost=[]\n",
    "child.append(0)\n",
    "adult.append(0)\n",
    "senior.append(0)\n",
    "totalCost.append(0)\n",
    "total=0\n",
    "\n",
    "cardno = []\n",
    "name= []\n",
    "expirydate= []\n",
    "cvv=[]\n",
    "cardno.append(0)\n",
    "name.append(0)\n",
    "expirydate.append(0)\n",
    "cvv.append(0)\n",
    "\n",
    "num_of_tickets=0\n",
    "category=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "PG-6fIbu0qe9"
   },
   "outputs": [],
   "source": [
    "#import Ticket\n",
    "#import Checkout\n",
    "\n",
    "h = Ticket()\n",
    "h.setSeniorTicketPrice(50)\n",
    "h.setChildTicketPrice(25)\n",
    "h.setAdultTicketPrice(100)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "hYrIt7680v3W"
   },
   "outputs": [],
   "source": [
    "def messagefirst():\n",
    "    for j in range(0,50):\n",
    "        print(\"@\",end=\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "aRMXaSJ403Sp"
   },
   "outputs": [],
   "source": [
    "def message():\n",
    "    print()\n",
    "    print()\n",
    "    print(\"Ticket Sales\")\n",
    "    print(\"Program Developer == ABC\")\n",
    "    print(\"Student ID = 123456 \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "b9BIBR_b04GG"
   },
   "outputs": [],
   "source": [
    "\n",
    "def menu():\n",
    "    number_of_senior_tickets = 0\n",
    "    number_of_adult_tickets = 0\n",
    "    number_of_child_tickets =0\n",
    "    number_of_concession_tickets = 0\n",
    "    print(\"Type of Tickets\")\n",
    "    print()\n",
    "    print(\"1. Child\")\n",
    "    print(\"2. Adult\")\n",
    "    print(\"3. Senior citizen/Concession\")\n",
    "    \n",
    "    n = int(input())\n",
    "    a = [1,2,3]\n",
    "    while(n in a):\n",
    "        if(n==1):\n",
    "            print(\"Number of Child tickets\")\n",
    "            number_of_child_tickets = int(input())\n",
    "            child[0] = number_of_child_tickets\n",
    "            print(\"Do you want to add more tickets?(Y/N)\")\n",
    "            choice = input()\n",
    "            if(choice.lower()=='y'):\n",
    "                menu()\n",
    "                break\n",
    "            else:\n",
    "                bill()\n",
    "                break\n",
    "        elif (n==2):\n",
    "            print(\"Number of Adult tickets\")\n",
    "            number_of_adult_tickets = int(input())\n",
    "            adult[0] = number_of_adult_tickets\n",
    "            print(\"Do you want to add more tickets?(Y/N)\")\n",
    "            choice = input()\n",
    "            if (choice.lower() == 'y'):\n",
    "                menu()\n",
    "                break\n",
    "            else:\n",
    "                bill()\n",
    "                break\n",
    "        elif(n==3):\n",
    "            print(\"Number of Senior Citizen tickets/Concession\")\n",
    "            number_of_senior_tickets = int(input())\n",
    "            senior[0] = number_of_senior_tickets\n",
    "            print(\"Do you want to add more tickets?(Y/N)\")\n",
    "            choice = input()\n",
    "            if (choice.lower() == 'y'):\n",
    "                menu()\n",
    "                break\n",
    "            else:\n",
    "                bill()\n",
    "                break\n",
    "        \n",
    "        else:\n",
    "            print(\"Please enter valid number\")\n",
    "            menu()\n",
    "            break "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 34
    },
    "colab_type": "code",
    "id": "D8TB-JSk2bfo",
    "outputId": "827b46d0-b4ac-4000-b4dd-288c836349b2"
   },
   "outputs": [],
   "source": [
    "def bill():\n",
    " \n",
    "    print(\"Price of \"  + str(child[0]) + \" child tickets \" + \" : \" + str(h.getChildTicketPrice()) +\n",
    "          \" * \" + str(child[0]) + \" = \" + str(h.getChildTicketPrice()*child[0]) + \" dollars\")\n",
    "    print(\"Price of \" + str(adult[0]) + \" Adult tickets \" + \" : \" + str(h.getAdultTicketPrice()) +\n",
    "          \" * \" + str(adult[0]) + \" = \" + str(h.getAdultTicketPrice() * adult[0]) + \" dollars\")\n",
    "    print(\"Price of \" + str(senior[0]) + \" senior tickets/concession \" + \" : \" + str(h.getSeniorTicketPrice()) +\n",
    "          \" * \" + str(senior[0]) + \" = \" + str(h.getSeniorTicketPrice() * senior[0]) + \" dollars\")\n",
    "\n",
    "\n",
    "    total = child[0]*h.getChildTicketPrice() + adult[0]*h.getAdultTicketPrice()+senior[0]*h.getSeniorTicketPrice()\n",
    "    totalCost[0] = total\n",
    "    print(\"Total Amount to pay:\")\n",
    "    print(total)\n",
    "\n",
    "    f = open(\"output.txt\", \"w\")\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "check = Checkout()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "kInWx86s9xzc"
   },
   "outputs": [],
   "source": [
    "def payment():\n",
    "#Card credentials\n",
    " print(\"Enter Your card details to Pay \")\n",
    " cardno = input(\"Enter Credit card number \")\n",
    " name = input(\"name on your card:\")\n",
    " expirydate = input(\"Valid through: \")\n",
    " cvv= input(\"CVV number: \")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 248
    },
    "colab_type": "code",
    "id": "7Bzj6RIsAi1G",
    "outputId": "5cecc256-6c82-4e28-a1d6-e3f272cd5e0d"
   },
   "outputs": [],
   "source": [
    "def display():\n",
    " \n",
    "#Display & writing into text file\n",
    " print(\"Your ticket confirmed \\n\")\n",
    "file1 = open(\"transactions.txt\",\"w\")\n",
    "l = [\"\\nNumber of child Tickets: \" + str(child[0])\n",
    "                     +\" \\nNumber of Adult tickets : \" + str(adult[0])+\n",
    "                     \" \\nNumber of Senior Citizen tickets: \"+ str(senior[0])\n",
    "                     +\" \\nTotal Cost = \" + str(totalCost[0]) + \" dollars\"]\n",
    "                     \n",
    "file1.writelines(l)\n",
    "file1.close()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 880
    },
    "colab_type": "code",
    "id": "dl-EolpBBYgA",
    "outputId": "c9232300-91df-4f1d-cf0a-57858bf691ae"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n",
      "\n",
      "Ticket Sales\n",
      "Program Developer == ABC\n",
      "Student ID = 123456 \n",
      "\n",
      "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n",
      "Type of Tickets\n",
      "\n",
      "1. Child\n",
      "2. Adult\n",
      "3. Senior citizen/Concession\n",
      "1\n",
      "Number of Child tickets\n",
      "1\n",
      "Do you want to add more tickets?(Y/N)\n",
      "n\n",
      "Price of 1 child tickets  : 25 * 1 = 25 dollars\n",
      "Price of 2 Adult tickets  : 100 * 2 = 200 dollars\n",
      "Price of 3 senior tickets/concession  : 50 * 3 = 150 dollars\n",
      "Total Amount to pay:\n",
      "375\n",
      "Enter Your card details to Pay \n",
      "Enter Credit card number 1234\n",
      "name on your card:abc\n",
      "Valid through: 122020\n",
      "CVV number: 789\n",
      "Your ticket confirmed \n",
      "\n"
     ]
    }
   ],
   "source": [
    "messagefirst()\n",
    "message()\n",
    "messagefirst()\n",
    "print()\n",
    "menu()\n",
    "payment()\n",
    "display()"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [],
   "name": "Untitled7.ipynb",
   "provenance": []
  },
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
