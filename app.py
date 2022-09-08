{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c5cad447",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, redirect, url_for\n",
    "\n",
    "from flask_pymongo import PyMongo\n",
    "\n",
    "import scraping\n",
    "\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a9a7381a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask-pymongo in c:\\users\\snapi\\anaconda3\\lib\\site-packages (2.3.0)\n",
      "Requirement already satisfied: Flask>=0.11 in c:\\users\\snapi\\anaconda3\\lib\\site-packages (from flask-pymongo) (1.1.2)\n",
      "Requirement already satisfied: PyMongo>=3.3 in c:\\users\\snapi\\anaconda3\\lib\\site-packages (from flask-pymongo) (4.2.0)\n",
      "Requirement already satisfied: click>=5.1 in c:\\users\\snapi\\anaconda3\\lib\\site-packages (from Flask>=0.11->flask-pymongo) (8.0.4)\n",
      "Requirement already satisfied: Werkzeug>=0.15 in c:\\users\\snapi\\anaconda3\\lib\\site-packages (from Flask>=0.11->flask-pymongo) (2.0.3)\n",
      "Requirement already satisfied: itsdangerous>=0.24 in c:\\users\\snapi\\anaconda3\\lib\\site-packages (from Flask>=0.11->flask-pymongo) (2.0.1)\n",
      "Requirement already satisfied: Jinja2>=2.10.1 in c:\\users\\snapi\\anaconda3\\lib\\site-packages (from Flask>=0.11->flask-pymongo) (2.11.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\snapi\\anaconda3\\lib\\site-packages (from click>=5.1->Flask>=0.11->flask-pymongo) (0.4.5)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\snapi\\anaconda3\\lib\\site-packages (from Jinja2>=2.10.1->Flask>=0.11->flask-pymongo) (2.0.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install flask-pymongo\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c07321bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flask_pymongo to set up mongo connection\n",
    "\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "225b9d26",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "\n",
    "def index():\n",
    "    \n",
    "    mars = mongo.db.mars.find_one()\n",
    "        \n",
    "    return render_template(\"index.html\", mars=mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b102ef40",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/scrape\")\n",
    "\n",
    "def scrape():\n",
    "    \n",
    "    mars = mongo.db.mars\n",
    "\n",
    "    mars_data = scraping.scrape_all()\n",
    "    \n",
    "    mars.update_one({}, {\"$set\":mars_data}, upsert=True)\n",
    "\n",
    "    return redirect('/', code=302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "717674a3",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1542321696.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [6]\u001b[1;36m\u001b[0m\n\u001b[1;33m    .update_one(query_parameter, {\"$set\": data}, options)\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    ".update_one(query_parameter, {\"$set\": data}, options)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ba3a470",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21a60ba2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
