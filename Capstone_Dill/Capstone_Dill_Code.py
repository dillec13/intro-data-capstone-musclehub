{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone Project 1: MuscleHub AB Test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Get started with SQL"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Like most businesses, Janet keeps her data in a SQL database.  Normally, you'd download the data from her database to a csv file, and then load it into a Jupyter Notebook using Pandas.\n",
    "\n",
    "For this project, you'll have to access SQL in a slightly different way.  You'll be using a special Codecademy library that lets you type SQL queries directly into this Jupyter notebook.  You'll have pass each SQL query as an argument to a function called `sql_query`.  Each query will return a Pandas DataFrame.  Here's an example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# This import only needs to happen once, at the beginning of the notebook\n",
    "from codecademySQL import sql_query"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>visit_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Karen</td>\n",
       "      <td>Manning</td>\n",
       "      <td>Karen.Manning@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Annette</td>\n",
       "      <td>Boone</td>\n",
       "      <td>AB9982@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>Merritt</td>\n",
       "      <td>SalvadorMerritt12@outlook.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Martha</td>\n",
       "      <td>Maxwell</td>\n",
       "      <td>Martha.Maxwell@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Andre</td>\n",
       "      <td>Mayer</td>\n",
       "      <td>AndreMayer90@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                          email  gender  \\\n",
       "0      0      Karen   Manning        Karen.Manning@gmail.com  female   \n",
       "1      1    Annette     Boone               AB9982@gmail.com  female   \n",
       "2      2   Salvador   Merritt  SalvadorMerritt12@outlook.com    male   \n",
       "3      3     Martha   Maxwell       Martha.Maxwell@gmail.com  female   \n",
       "4      4      Andre     Mayer         AndreMayer90@gmail.com    male   \n",
       "\n",
       "  visit_date  \n",
       "0     5-1-17  \n",
       "1     5-1-17  \n",
       "2     5-1-17  \n",
       "3     5-1-17  \n",
       "4     5-1-17  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Here's an example of a query that just displays some data\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Here's an example where we save the data to a DataFrame\n",
    "df = sql_query('''\n",
    "SELECT *\n",
    "FROM applications\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Get your dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's get started!\n",
    "\n",
    "Janet of MuscleHub has a SQLite database, which contains several tables that will be helpful to you in this investigation:\n",
    "- `visits` contains information about potential gym customers who have visited MuscleHub\n",
    "- `fitness_tests` contains information about potential customers in \"Group A\", who were given a fitness test\n",
    "- `applications` contains information about any potential customers (both \"Group A\" and \"Group B\") who filled out an application.  Not everyone in `visits` will have filled out an application.\n",
    "- `purchases` contains information about customers who purchased a membership to MuscleHub.\n",
    "\n",
    "Use the space below to examine each table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>visit_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Karen</td>\n",
       "      <td>Manning</td>\n",
       "      <td>Karen.Manning@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Annette</td>\n",
       "      <td>Boone</td>\n",
       "      <td>AB9982@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>Merritt</td>\n",
       "      <td>SalvadorMerritt12@outlook.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Martha</td>\n",
       "      <td>Maxwell</td>\n",
       "      <td>Martha.Maxwell@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Andre</td>\n",
       "      <td>Mayer</td>\n",
       "      <td>AndreMayer90@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                          email  gender  \\\n",
       "0      0      Karen   Manning        Karen.Manning@gmail.com  female   \n",
       "1      1    Annette     Boone               AB9982@gmail.com  female   \n",
       "2      2   Salvador   Merritt  SalvadorMerritt12@outlook.com    male   \n",
       "3      3     Martha   Maxwell       Martha.Maxwell@gmail.com  female   \n",
       "4      4      Andre     Mayer         AndreMayer90@gmail.com    male   \n",
       "\n",
       "  visit_date  \n",
       "0     5-1-17  \n",
       "1     5-1-17  \n",
       "2     5-1-17  \n",
       "3     5-1-17  \n",
       "4     5-1-17  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine visits here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>fitness_test_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Kim</td>\n",
       "      <td>Walter</td>\n",
       "      <td>KimWalter58@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Tom</td>\n",
       "      <td>Webster</td>\n",
       "      <td>TW3857@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Marcus</td>\n",
       "      <td>Bauer</td>\n",
       "      <td>Marcus.Bauer@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Best</td>\n",
       "      <td>RB6305@hotmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Carrie</td>\n",
       "      <td>Francis</td>\n",
       "      <td>CF1896@hotmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-05</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                   email  gender  \\\n",
       "0      0        Kim    Walter   KimWalter58@gmail.com  female   \n",
       "1      1        Tom   Webster        TW3857@gmail.com    male   \n",
       "2      2     Marcus     Bauer  Marcus.Bauer@gmail.com    male   \n",
       "3      3    Roberta      Best      RB6305@hotmail.com  female   \n",
       "4      4     Carrie   Francis      CF1896@hotmail.com  female   \n",
       "\n",
       "  fitness_test_date  \n",
       "0        2017-07-03  \n",
       "1        2017-07-02  \n",
       "2        2017-07-01  \n",
       "3        2017-07-02  \n",
       "4        2017-07-05  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine fitness_tests here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM fitness_tests\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>application_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Roy</td>\n",
       "      <td>Abbott</td>\n",
       "      <td>RoyAbbott32@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-08-12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Agnes</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>AgnesAcevedo1@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>RA8063@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Darren</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>DAcosta1996@hotmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Vernon</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>VAcosta1975@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                    email  gender  \\\n",
       "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male   \n",
       "1      1      Agnes   Acevedo  AgnesAcevedo1@gmail.com  female   \n",
       "2      2    Roberta   Acevedo         RA8063@gmail.com  female   \n",
       "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male   \n",
       "4      4     Vernon    Acosta    VAcosta1975@gmail.com    male   \n",
       "\n",
       "  application_date  \n",
       "0       2017-08-12  \n",
       "1       2017-09-29  \n",
       "2       2017-09-15  \n",
       "3       2017-07-26  \n",
       "4       2017-07-14  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine applications here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM applications\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>purchase_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Roy</td>\n",
       "      <td>Abbott</td>\n",
       "      <td>RoyAbbott32@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-08-18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>RA8063@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Vernon</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>VAcosta1975@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Darren</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>DAcosta1996@hotmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Dawn</td>\n",
       "      <td>Adkins</td>\n",
       "      <td>Dawn.Adkins@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-08-24</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                    email  gender purchase_date\n",
       "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male    2017-08-18\n",
       "1      1    Roberta   Acevedo         RA8063@gmail.com  female    2017-09-16\n",
       "2      2     Vernon    Acosta    VAcosta1975@gmail.com    male    2017-07-20\n",
       "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male    2017-07-27\n",
       "4      4       Dawn    Adkins    Dawn.Adkins@gmail.com  female    2017-08-24"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine purchases here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM purchases\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'd like to download a giant DataFrame containing all of this data.  You'll need to write a query that does the following things:\n",
    "\n",
    "1. Not all visits in  `visits` occurred during the A/B test.  You'll only want to pull data where `visit_date` is on or after `7-1-17`.\n",
    "\n",
    "2. You'll want to perform a series of `LEFT JOIN` commands to combine the four tables that we care about.  You'll need to perform the joins on `first_name`, `last_name`, and `email`.  Pull the following columns:\n",
    "\n",
    "\n",
    "- `visits.first_name`\n",
    "- `visits.last_name`\n",
    "- `visits.gender`\n",
    "- `visits.email`\n",
    "- `visits.visit_date`\n",
    "- `fitness_tests.fitness_test_date`\n",
    "- `applications.application_date`\n",
    "- `purchases.purchase_date`\n",
    "\n",
    "Save the result of this query to a variable called `df`.\n",
    "\n",
    "Hint: your result should have 5004 rows.  Does it?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5004"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = sql_query('''\n",
    "SELECT visits.first_name,\n",
    "        visits.last_name,\n",
    "        visits.gender,\n",
    "        visits.email,\n",
    "        visits.visit_date,\n",
    "        fitness_tests.fitness_test_date,\n",
    "        applications.application_date,\n",
    "        purchases.purchase_date\n",
    "FROM visits\n",
    "LEFT JOIN fitness_tests\n",
    "    ON fitness_tests.first_name = visits.first_name\n",
    "    AND fitness_tests.last_name = visits.last_name\n",
    "    AND fitness_tests.email = visits.email\n",
    "LEFT JOIN applications\n",
    "    ON applications.first_name = visits.first_name\n",
    "    AND applications.last_name = visits.last_name\n",
    "    AND applications.email = visits.email\n",
    "LEFT JOIN purchases\n",
    "    ON purchases.first_name = visits.first_name\n",
    "    AND purchases.last_name = visits.last_name\n",
    "    AND purchases.email = visits.email\n",
    "WHERE visits.visit_date >= '7-1-17'\n",
    "''')\n",
    "len(df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Investigate the A and B groups"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have some data to work with! Import the following modules so that we can start doing analysis:\n",
    "- `import pandas as pd`\n",
    "- `from matplotlib import pyplot as plt`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to add some columns to `df` to help us with our analysis.\n",
    "\n",
    "Start by adding a column called `ab_test_group`.  It should be `A` if `fitness_test_date` is not `None`, and `B` if `fitness_test_date` is `None`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['ab_test_group'] = df.fitness_test_date.apply(lambda x:\n",
    "                                                'A' if pd.notnull(x) else 'B')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's do a quick sanity check that Janet split her visitors such that about half are in A and half are in B.\n",
    "\n",
    "Start by using `groupby` to count how many users are in each `ab_test_group`.  Save the results to `ab_counts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>first_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>2504</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>2500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  ab_test_group  first_name\n",
       "0             A        2504\n",
       "1             B        2500"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ab_counts = df.groupby('ab_test_group').first_name.count().reset_index()\n",
    "ab_counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'll want to include this information in our presentation.  Let's create a pie cart using `plt.pie`.  Make sure to include:\n",
    "- Use `plt.axis('equal')` so that your pie chart looks nice\n",
    "- Add a legend labeling `A` and `B`\n",
    "- Use `autopct` to label the percentage of each group\n",
    "- Save your figure as `ab_test_pie_chart.png`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x110a38290>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.pie(ab_counts.first_name.values, labels=['A', 'B'], autopct='%0.2f%%',\n",
    "        colors = ['#0070C0','#eb8f22'])\n",
    "plt.axis('equal')\n",
    "plt.savefig('ab_test_pie_chart.png')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Who picks up an application?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Recall that the sign-up process for MuscleHub has several steps:\n",
    "1. Take a fitness test with a personal trainer (only Group A)\n",
    "2. Fill out an application for the gym\n",
    "3. Send in their payment for their first month's membership\n",
    "\n",
    "Let's examine how many people make it to Step 2, filling out an application.\n",
    "\n",
    "Start by creating a new column in `df` called `is_application` which is `Application` if `application_date` is not `None` and `No Application`, otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df['is_application'] = df.application_date.apply(lambda x:\n",
    "                                                'Application' if pd.notnull(x) else 'No Application')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, using `groupby`, count how many people from Group A and Group B either do or don't pick up an application.  You'll want to group by `ab_test_group` and `is_application`.  Save this new DataFrame as `app_counts`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "app_counts = df.groupby(['ab_test_group','is_application']).first_name.count().reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to want to calculate the percent of people in each group who complete an application.  It's going to be much easier to do this if we pivot `app_counts` such that:\n",
    "- The `index` is `ab_test_group`\n",
    "- The `columns` are `is_application`\n",
    "Perform this pivot and save it to the variable `app_pivot`.  Remember to call `reset_index()` at the end of the pivot!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>is_application</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Application</th>\n",
       "      <th>No Application</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>250</td>\n",
       "      <td>2254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>325</td>\n",
       "      <td>2175</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_application ab_test_group  Application  No Application\n",
       "0                          A          250            2254\n",
       "1                          B          325            2175"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "app_pivot = app_counts.pivot(columns='is_application',\n",
    "                            index='ab_test_group',\n",
    "                            values='first_name')\\\n",
    "            .reset_index()\n",
    "app_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Define a new column called `Total`, which is the sum of `Application` and `No Application`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "app_pivot['Total'] = app_pivot.Application + app_pivot['No Application']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate another column called `Percent with Application`, which is equal to `Application` divided by `Total`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>is_application</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Application</th>\n",
       "      <th>No Application</th>\n",
       "      <th>Total</th>\n",
       "      <th>Percent with Application</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>250</td>\n",
       "      <td>2254</td>\n",
       "      <td>2504</td>\n",
       "      <td>9.984026</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>325</td>\n",
       "      <td>2175</td>\n",
       "      <td>2500</td>\n",
       "      <td>13.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_application ab_test_group  Application  No Application  Total  \\\n",
       "0                          A          250            2254   2504   \n",
       "1                          B          325            2175   2500   \n",
       "\n",
       "is_application  Percent with Application  \n",
       "0                               9.984026  \n",
       "1                              13.000000  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "app_pivot['Percent with Application'] = 100 * app_pivot.Application / app_pivot.Total\n",
    "app_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like more people from Group B turned in an application.  Why might that be?\n",
    "\n",
    "We need to know if this difference is statistically significant.\n",
    "\n",
    "Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10.893961295282612,\n",
       " 0.00096478276007223038,\n",
       " 1,\n",
       " array([[  287.72981615,  2216.27018385],\n",
       "        [  287.27018385,  2212.72981615]]))"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scipy.stats import chi2_contingency\n",
    "\n",
    "contingency = [[250, 2254], [325, 2175]]\n",
    "chi2_contingency(contingency)\n",
    "\n",
    "# Note that when run, the second output is the p-value.  In this instance, the result is 0.0009648, which is less than 0.05.\n",
    "# For this test, our null hypothesis is that there is no difference between groups A and B.\n",
    "# Since we have a p-value less than 5, we can therefore reject the null hypothesis and state that there is a significant \n",
    "# difference. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Who purchases a membership?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Of those who picked up an application, how many purchased a membership?\n",
    "\n",
    "Let's begin by adding a column to `df` called `is_member` which is `Member` if `purchase_date` is not `None`, and `Not Member` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df['is_member'] = df.purchase_date.apply(lambda x:\n",
    "                                        'Member' if pd.notnull(x) else 'Not Member')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let's create a DataFrame called `just_apps` the contains only people who picked up an application."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>gender</th>\n",
       "      <th>email</th>\n",
       "      <th>visit_date</th>\n",
       "      <th>fitness_test_date</th>\n",
       "      <th>application_date</th>\n",
       "      <th>purchase_date</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>is_application</th>\n",
       "      <th>is_member</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Edward</td>\n",
       "      <td>Bowen</td>\n",
       "      <td>male</td>\n",
       "      <td>Edward.Bowen@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>None</td>\n",
       "      <td>2017-07-04</td>\n",
       "      <td>2017-07-04</td>\n",
       "      <td>B</td>\n",
       "      <td>Application</td>\n",
       "      <td>Member</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Marcus</td>\n",
       "      <td>Bauer</td>\n",
       "      <td>male</td>\n",
       "      <td>Marcus.Bauer@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-01</td>\n",
       "      <td>2017-07-03</td>\n",
       "      <td>2017-07-05</td>\n",
       "      <td>A</td>\n",
       "      <td>Application</td>\n",
       "      <td>Member</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Salvador</td>\n",
       "      <td>Cardenas</td>\n",
       "      <td>male</td>\n",
       "      <td>SCardenas1980@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-07</td>\n",
       "      <td>2017-07-06</td>\n",
       "      <td>None</td>\n",
       "      <td>A</td>\n",
       "      <td>Application</td>\n",
       "      <td>Not Member</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Valerie</td>\n",
       "      <td>Munoz</td>\n",
       "      <td>female</td>\n",
       "      <td>VMunoz1998@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>2017-07-03</td>\n",
       "      <td>2017-07-05</td>\n",
       "      <td>2017-07-06</td>\n",
       "      <td>A</td>\n",
       "      <td>Application</td>\n",
       "      <td>Member</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>Michael</td>\n",
       "      <td>Burks</td>\n",
       "      <td>male</td>\n",
       "      <td>MB9820@gmail.com</td>\n",
       "      <td>7-1-17</td>\n",
       "      <td>None</td>\n",
       "      <td>2017-07-07</td>\n",
       "      <td>2017-07-13</td>\n",
       "      <td>B</td>\n",
       "      <td>Application</td>\n",
       "      <td>Member</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   first_name last_name  gender                    email visit_date  \\\n",
       "2      Edward     Bowen    male   Edward.Bowen@gmail.com     7-1-17   \n",
       "3      Marcus     Bauer    male   Marcus.Bauer@gmail.com     7-1-17   \n",
       "9    Salvador  Cardenas    male  SCardenas1980@gmail.com     7-1-17   \n",
       "11    Valerie     Munoz  female     VMunoz1998@gmail.com     7-1-17   \n",
       "35    Michael     Burks    male         MB9820@gmail.com     7-1-17   \n",
       "\n",
       "   fitness_test_date application_date purchase_date ab_test_group  \\\n",
       "2               None       2017-07-04    2017-07-04             B   \n",
       "3         2017-07-01       2017-07-03    2017-07-05             A   \n",
       "9         2017-07-07       2017-07-06          None             A   \n",
       "11        2017-07-03       2017-07-05    2017-07-06             A   \n",
       "35              None       2017-07-07    2017-07-13             B   \n",
       "\n",
       "   is_application   is_member  \n",
       "2     Application      Member  \n",
       "3     Application      Member  \n",
       "9     Application  Not Member  \n",
       "11    Application      Member  \n",
       "35    Application      Member  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "just_apps = df[df.is_application == 'Application']\n",
    "just_apps.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Now, let's do a `groupby` to find out how many people in `just_apps` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>is_member</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Member</th>\n",
       "      <th>Not Member</th>\n",
       "      <th>Total</th>\n",
       "      <th>Percent Purchase</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>200</td>\n",
       "      <td>50</td>\n",
       "      <td>250</td>\n",
       "      <td>0.800000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>250</td>\n",
       "      <td>75</td>\n",
       "      <td>325</td>\n",
       "      <td>0.769231</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_member ab_test_group  Member  Not Member  Total  Percent Purchase\n",
       "0                     A     200          50    250          0.800000\n",
       "1                     B     250          75    325          0.769231"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "member_count = just_apps.groupby(['ab_test_group', 'is_member'])\\\n",
    "                 .first_name.count().reset_index()\n",
    "member_pivot = member_count.pivot(columns='is_member',\n",
    "                                  index='ab_test_group',\n",
    "                                  values='first_name')\\\n",
    "                           .reset_index()\n",
    "\n",
    "member_pivot['Total'] = member_pivot.Member + member_pivot['Not Member']\n",
    "member_pivot['Percent Purchase'] = member_pivot.Member / member_pivot.Total\n",
    "member_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like people who took the fitness test were more likely to purchase a membership **if** they picked up an application.  Why might that be?\n",
    "\n",
    "Just like before, we need to know if this difference is statistically significant.  Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.61586923076923095,\n",
       " 0.43258646051083327,\n",
       " 1,\n",
       " array([[ 195.65217391,   54.34782609],\n",
       "        [ 254.34782609,   70.65217391]]))"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "contingency = [[200, 50], [250, 75]]\n",
    "chi2_contingency(contingency)\n",
    "\n",
    "#The result is not significant."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, we looked at what percent of people **who picked up applications** purchased memberships.  What we really care about is what percentage of **all visitors** purchased memberships.  Return to `df` and do a `groupby` to find out how many people in `df` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `final_member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>is_member</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Member</th>\n",
       "      <th>Not Member</th>\n",
       "      <th>Total</th>\n",
       "      <th>Percent Purchase</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>200</td>\n",
       "      <td>2304</td>\n",
       "      <td>2504</td>\n",
       "      <td>0.079872</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>250</td>\n",
       "      <td>2250</td>\n",
       "      <td>2500</td>\n",
       "      <td>0.100000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_member ab_test_group  Member  Not Member  Total  Percent Purchase\n",
       "0                     A     200        2304   2504          0.079872\n",
       "1                     B     250        2250   2500          0.100000"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_member_count = df.groupby(['ab_test_group', 'is_member'])\\\n",
    "                 .first_name.count().reset_index()\n",
    "final_member_pivot = final_member_count.pivot(columns='is_member',\n",
    "                                  index='ab_test_group',\n",
    "                                  values='first_name')\\\n",
    "                           .reset_index()\n",
    "\n",
    "final_member_pivot['Total'] = final_member_pivot.Member + final_member_pivot['Not Member']\n",
    "final_member_pivot['Percent Purchase'] = final_member_pivot.Member / final_member_pivot.Total\n",
    "final_member_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, when we only considered people who had **already picked up an application**, we saw that there was no significant difference in membership between Group A and Group B.\n",
    "\n",
    "Now, when we consider all people who **visit MuscleHub**, we see that there might be a significant different in memberships between Group A and Group B.  Perform a significance test and check."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5.9491822925911562,\n",
       " 0.014724114645783203,\n",
       " 1,\n",
       " array([[  225.17985612,  2278.82014388],\n",
       "        [  224.82014388,  2275.17985612]]))"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "contingency = [[200, 2304], [250, 2250]]\n",
    "chi2_contingency(contingency)\n",
    "\n",
    "# The result is significant."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Summarize the acquisition funel with a chart"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'd like to make a bar chart for Janet that shows the difference between Group A (people who were given the fitness test) and Group B (people who were not given the fitness test) at each state of the process:\n",
    "- Percent of visitors who apply\n",
    "- Percent of applicants who purchase a membership\n",
    "- Percent of visitors who purchase a membership\n",
    "\n",
    "Create one plot for **each** of the three sets of percentages that you calculated in `app_pivot`, `member_pivot` and `final_member_pivot`.  Each plot should:\n",
    "- Label the two bars as `Fitness Test` and `No Fitness Test`\n",
    "- Make sure that the y-axis ticks are expressed as percents (i.e., `5%`)\n",
    "- Have a title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1a1a3d9810>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Percent of Visitors who Apply\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(app_pivot)),\n",
    "       app_pivot['Percent with Application'].values,\n",
    "        color = ['#0070C0','#eb8f22'])\n",
    "ax.set_xticks(range(len(app_pivot)))\n",
    "ax.set_xticklabels(['Fitness Test', 'No Fitness Test'])\n",
    "ax.set_yticks([0, 5, 10, 15, 20])\n",
    "ax.set_yticklabels(['0%', '5%', '10%', '15%', '20%'])\n",
    "plt.savefig('percent_visitors_apply.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYMAAAD8CAYAAACVZ8iyAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4xLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvAOZPmwAAGOpJREFUeJzt3Xm0XWWd5vHvI5NhUAYvLAbjgFmopTJdKSxFLbFUuqDAAhQZKgp2rF6WiKJIt6BQYgPdIOBahd2hsA04YIhDUCOYSlFKaYMkhimgBmkLMWkSSyilsTSYX/+x35hjkpvh7ntzQb6ftc7ae7/n3ee8J9n3POfd7zn7TVUhSXpye8pEN0CSNPEMA0mSYSBJMgwkSRgGkiQMA0kSGxEGST6ZZFmSuwbKdk4yN8nittyplSfJx5Pcm+SOJAe08n2SLEhye5KXtbItk/xDkm3H68VJkjbOxvQMPgW8YY2yM4F5VTUFmNe2AQ4DprTbNOATrfwdrc4xwPta2X8Crq6qR0fbeEnS2NhgGFTVt4Cfr1F8JDCjrc8Ajhoov6o6NwM7JtkdWAFMArYFViTZETgCuKr/S5Ak9bXlKPfbraqWAlTV0iS7tvI9gZ8M1Huglf0d3Rv/NnS9hA8BH60N/Pw5yTS6Hgbbbbfdgc9//vNH2VxJenJasGDBz6pqaEP1RhsGI8k6yqqq7gdeDZDkecAewPeTXA1sDZxdVT9cx47TgekAw8PDNX/+/DFuriT9YUvyLxtTb7TfJnqwnf6hLZe18geAZw7U2wtYssa+HwXOBk4FPgN8uN0kSRNktGFwHTC1rU8FZg+U/1X7VtHBwL+tOp0EkORVwE+rajHd+MFK4LdtXZI0QTZ4mijJ5+hO8TwjyQN0n+IvAGYmOQW4Hzi2VZ8D/AfgXuBR4G0DjxPgLOBNrWg6Xc9gS7pvFkmSJkieKJewdsxAkjZdkgVVNbyhev4CWZJkGEiSDANJEoaBJAnDQJKEYSBJwjCQJGEYSJIwDCRJGAaSJAwDSRKGgSQJw0CSRM8wSPLuJHclWZTktFa2c5K5SRa35U6t/OhW76Yku7SyvZNc0/9lSJL6GHUYJHkR8B+Bg4B9gcOTTAHOBOZV1RRgXtsGOB04mG4u5ONb2Xl0s55JkiZQn57BC4Cbq+rRqnoM+CbwRuBIYEarMwM4qq2vBLahm9VsRZJDgKVt1jNJ0gTa4Exn63EX8NF2yudXdDOczQd2WzXVZVUtTbJrq38ucAPdnMgnAjOB49b3BEmmAdMAJk+e3KOpkqT1GXXPoKruAS4E5gLXA7cDj62n/tyqOrCqjqDrLcwB9kkyK8kVSdaaB7mqplfVcFUNDw0NjbapkqQN6DWAXFVXVtUBVfVK4OfAYuDBJLsDtOWywX3am/5U4HLgfOBkYAFwQp+2SJJGr++3iXZty8nAXwKfA66je7OnLWevsdsZwGVVtQKYBBTdeMJaPQNJ0ubRZ8wA4AttzGAF8M6qeijJBcDMJKcA9wPHrqqcZA9guKrOaUUXAzcDD7N6oFmStJmlqia6DRtleHi45s+fP9HNkKQnlCQLqmp4Q/X8BbIkyTCQJBkGkiQMA0kShoEkCcNAkoRhIEnCMJAkYRhIkjAMJEkYBpIkDANJEoaBJIn+8xm8J8miJHcl+VySpyZ5TpJbkixO8vkkW7e672r15gyUvSLJx8bihUiSRm/UYZBkT+BUuvkJXgRsQTen8YXAJVU1BXgIOKXt8nbgJcBC4PVJApwNfGT0zZckjYW+p4m2BCYl2ZJuprKlwGuAWe3+Gfz+pDVbtXorgJOAOVX1UM82SJJ6GvVMZ1X10yQX0c1m9ivgG3RzGT9cVY+1ag8Ae7b1i+hmNVsEfBv4MvCG9T1HkmnANIDJkyePtqndY73nm7321x+uuuRVE90EacL1OU20E3Ak8BxgD2A74LB1VC2Aqrq6qvavqhOB9wIfBw5LMivJJUnWaktVTa+q4aoaHhoaGm1TJUkb0Oc00WuB/1NVy9vk9l8E/gTYsZ02AtgLWDK4U5sH+aVVNRs4C3gz8Gvg0B5tkST10CcM7gcOTrJtGww+FLgbuBE4ptWZCsxeY7+P0A0cA0yi6zmspBtLkCRNgFGHQVXdQjdQ/D3gzvZY04EPAO9Nci+wC3Dlqn2S7N/2XdiKrmz7HgBcP9q2SJL6GfUAMkBVfRj48BrF9wEHjVB/Iau/akpVXQpc2qcNkqT+/AWyJKlfz0DS2PnZpXtPdBP0OPWM03407s9hz0CSZBhIkgwDSRKGgSQJw0CShGEgScIwkCRhGEiSMAwkSRgGkiT6TW6zT5LbBm6/SHJakp2TzE2yuC13avWPTrIoyU1Jdmlleye5ZqxejCRpdPpcwvoHVbVfVe0HHAg8CnwJOBOYV1VTgHltG+B04GDgKuD4VnYeq+c2kCRNkLE6TXQo8KOq+he6qTBntPIZwFFtfSWwDd0kNiuSHAIsrarFY9QGSdIojdVVS48DPtfWd6uqpQBVtTTJrq38XOAGumkwTwRmtv0kSROsd88gydbAXwDXrq9eVc2tqgOr6gi63sIcYJ8ks5JckWStaS+TTEsyP8n85cuX922qJGkEY3Ga6DDge1X1YNt+MMnuAG25bLBye9OfClwOnA+cDCwATljzgatqelUNV9Xw0NDQGDRVkrQuYxEGb2H1KSKA6+je7GnL2WvUPwO4rKpWAJOAohtPWKtnIEnaPHqNGbRP+X8GvGOg+AJgZpJTgPuBYwfq7wEMV9U5rehi4GbgYVYPNEuSNrNeYVBVjwK7rFH2r3TfLlpX/SXA4QPb17KBsQZJ0vjzF8iSJMNAkmQYSJIwDCRJGAaSJAwDSRKGgSQJw0CShGEgScIwkCRhGEiSMAwkSRgGkiR6hkGSHdtMZd9Pck+SlyXZOcncJIvbcqdW9+gki5LclGSXVrZ3kmvG4oVIkkavb8/gMuD6qno+sC9wD3AmMK+qpgDz2jbA6cDBwFXA8a3sPODsnm2QJPU06jBI8jTglcCVAFX1m6p6GDgSmNGqzWD1pDUrgW3oZjRbkeQQYGlVLR5tGyRJY6PP5DbPBZYD/yvJvnTzGL8b2K2qlgJU1dIku7b65wI3AEuAE4GZwHHre4Ik04BpAJMnT+7RVEnS+vQ5TbQlcADwiaraH/h/rD4ltJaqmltVB1bVEXS9hTnAPm3M4Yo2heaa+0yvquGqGh4aGurRVEnS+vQJgweAB6rqlrY9iy4cHkyyO0BbLhvcqb3pTwUuB84HTqbrVZzQoy2SpB5GHQZV9X+BnyTZpxUdCtwNXEf3Zk9bzl5j1zOAy6pqBTAJKLrxhLV6BpKkzaPPmAHAu4DPJNkauA94G13AzExyCnA/cOyqykn2AIar6pxWdDFwM/AwqweaJUmbWa8wqKrbgOF13HXoCPWXAIcPbF8LXNunDZKk/vwFsiTJMJAkGQaSJAwDSRKGgSQJw0CShGEgScIwkCRhGEiSMAwkSRgGkiQMA0kShoEkiZ5hkOTHSe5McluS+a1s5yRzkyxuy51a+dFJFiW5KckurWzvJNf0fxmSpD7Gomfwp1W1X1WtupT1mcC8qpoCzGP1VJinAwcDVwHHt7LzgLPHoA2SpB7G4zTRkcCMtj6D1ZPWrAS2oZvRbEWSQ4ClVbV4HNogSdoEfWc6K+AbSQr4n1U1HditqpYCVNXSJLu2uucCNwBLgBOBmcBx63vwJNOAaQCTJ0/u2VRJ0kj6hsHLq2pJe8Ofm+T7I1WsqrnAXIAkU4E5wD5J3gc8BLy7qh5dY5/pwHSA4eHh6tlWSdIIep0matNYUlXLgC8BBwEPJtkdoC2XDe6TZFtgKnA5cD5wMrAAOKFPWyRJozfqMEiyXZIdVq0DrwPuAq6je7OnLWevsesZwGVVtQKYRHeqaSXdWIIkaQL0OU20G/ClJKse57NVdX2SW4GZSU4B7geOXbVDkj2A4ao6pxVdDNwMPMzqgWZJ0mY26jCoqvuAfddR/q/AoSPsswQ4fGD7WuDa0bZBkjQ2/AWyJMkwkCQZBpIkDANJEoaBJAnDQJKEYSBJwjCQJGEYSJIwDCRJGAaSJAwDSRKGgSSJMQiDJFskWZjkq237OUluSbI4yeeTbN3K35XkriRzBspekeRjfdsgSepnLHoG7wbuGdi+ELikqqbQTWd5Sit/O/ASYCHw+nQTIZwNfGQM2iBJ6qFXGCTZC/hz4O/bdoDXALNalRn8/qQ1W9HNaLYCOAmYU1UP9WmDJKm/vj2DS+mmsVzZtncBHq6qx9r2A8Cebf0iulnNhoBvs3oe5BElmZZkfpL5y5cv79lUSdJI+syBfDiwrKoWDBavo2oBVNXVVbV/VZ0IvBf4OHBYkllJLkmyVluqanpVDVfV8NDQ0GibKknagD49g5cDf5Hkx8A1dKeHLgV2TLJqOs29gCWDO7V5kF9aVbOBs4A3A79mhKkyJUnjb9RhUFX/uar2qqpnA8cB/1hVJwA3Ase0alOB2Wvs+hG6gWOASXQ9h5V0YwmSpAkwHr8z+ADw3iT30o0hXLnqjiT7A1TVwlZ0JXAncABw/Ti0RZK0EbbccJUNq6p/Av6prd8HHDRCvYWs/qopVXUp3aklSdIE8hfIkiTDQJJkGEiSMAwkSRgGkiQMA0kShoEkCcNAkoRhIEnCMJAkYRhIkjAMJEn0m9zmqUm+m+T2JIuSnNvKn5PkliSLk3w+ydat/F1J7koyZ6DsFUk+NjYvRZI0Wn16Br8GXlNV+wL7AW9IcjBwIXBJVU0BHmL1VUrfDrwEWAi8vs2XfDbd/AaSpAnUZ3KbqqpH2uZW7VZ0M57NauUzgKMGdtuKbhKbFcBJwJyqemi0bZAkjY1eYwZJtkhyG7AMmAv8CHi4qh5rVR4A9mzrFwE3A0PAt+lmQbu8z/NLksZGrzCoqt9W1X50cx0fBLxgXdVa3aurav+qOhF4L/Bx4LAks5JckmSttiSZlmR+kvnLly/v01RJ0nqMybeJquphupnODgZ2TLJqBrW9gCWDdZPsAby0qmYDZwFvpht/OHQdjzu9qoaranhoaGgsmipJWoc+3yYaSrJjW58EvBa4B7gROKZVmwrMXmPXj9ANHANMous5rKQbS5AkTYA+PYPdgRuT3AHcCsytqq8CHwDem+ReYBe6Se8BSLI//G4uZNp9dwIHANf3aIskqYctN1xl3arqDmD/dZTfRzd+sK59FrL6q6ZU1aXApaNtgyRpbPgLZEmSYSBJMgwkSRgGkiQMA0kShoEkCcNAkoRhIEnCMJAkYRhIkjAMJEkYBpIkDANJEv3mM3hmkhuT3JNkUZJ3t/Kdk8xNsrgtd2rlR7d6NyXZpZXtneSasXkpkqTR6tMzeAw4vapeQDfD2TuTvBA4E5hXVVOAeW0b4PRW7yrg+FZ2HqsnupEkTZBRh0FVLa2q77X1X9LNcrYncCQwo1WbARzV1lcC29DNaLYiySHA0qpaPNo2SJLGxqgntxmU5Nl0E93cAuxWVUuhC4wku7Zq5wI30M2JfCIwEzhuA487DZgGMHny5LFoqiRpHXoPICfZHvgCcFpV/WKkelU1t6oOrKoj6HoLc4B9ksxKckWSteZArqrpVTVcVcNDQ0N9mypJGkGvMEiyFV0QfKaqvtiKH0yye7t/d2DZGvtsC0wFLgfOB04GFgAn9GmLJGn0+nybKHQT2t9TVR8buOs6ujd72nL2GrueAVxWVSuASUDRjSes1TOQJG0efcYMXg6cBNyZ5LZW9l+AC4CZSU4B7geOXbVDkj2A4ao6pxVdDNwMPMzqgWZJ0mY26jCoqn8GMsLdh46wzxLg8IHta4FrR9sGSdLY8BfIkiTDQJJkGEiSMAwkSRgGkiQMA0kShoEkCcNAkoRhIEnCMJAkYRhIkjAMJEkYBpIk+k9u88kky5LcNVC2c5K5SRa35U6t/Ogki5LclGSXVrZ3kmv6vQRJUl99ewafAt6wRtmZwLyqmgLMa9sApwMHA1cBx7ey84Cze7ZBktRTrzCoqm8BP1+j+EhgRlufwepJa1YC29DNaLYiySHA0qpa3KcNkqT++sx0NpLdqmopQFUtTbJrKz8XuAFYApwIzASOW98DJZkGTAOYPHnyODRVkgSbcQC5quZW1YFVdQRdb2EOsE+SWUmuSLLWHMhVNb2qhqtqeGhoaHM1VZKedMYjDB5MsjtAWy4bvLO96U8FLgfOB04GFgAnjENbJEkbYTzC4Dq6N3vacvYa958BXFZVK4BJQNGNJ6zVM5AkbR69xgySfA54NfCMJA8AHwYuAGYmOQW4Hzh2oP4ewHBVndOKLgZuBh5m9UCzJGkz6xUGVfWWEe46dIT6S4DDB7avBa7t0wZJUn/+AlmSZBhIkgwDSRKGgSQJw0CShGEgScIwkCRhGEiSMAwkSRgGkiQMA0kShoEkCcNAksQ4hUGSNyT5QZJ7k5zZyj6T5I4k/3Wg3tlJjhyPNkiSNt6Yh0GSLYC/Aw4DXgi8JclLAKrqJcAhSZ7eZkE7qKrWnPxGkrSZ9ZrPYAQHAfdW1X0ASa4B/hyYlOQpwNbAb4G/BT40Ds8vSdpE4xEGewI/Gdh+APhjulnPvgdcDTwPSFUtXN8DJZkGTGubjyT5wdg390npGcDPJroRjxe5dKJboHXwGB30nvTZ+1kbU2k8wmBdra6qOu13FZKvAO9I8kFgX2BuVV2xjp2mA9PHoY1PaknmV9XwRLdDGonH6OY3HgPIDwDPHNjeC1iyaqMNGM8HtgNeVFVvAk5Ksu04tEWStBHGIwxuBaYkeU6SrYHjgOsAkmwFvBv478C2QA20Y+txaIskaSOM+Wmiqnosyd8ANwBbAJ+sqkXt7ncCM6rq0SR3AElyJzCnqh4e67ZoRJ560+Odx+hmlqracC1J0h80f4EsSTIMJEmGwYRL8tsktw3cnp1kOMnH2/2vTvInm7lNbxtoz2+S3NnWL9jEx9k5yV+PVzs1NpJUkosHtt+X5JxN2P+tSZYPHDNXtfK/TfLatn7a5v7GYJIvtfbcm+TfBtq3SX9PSV6T5ODxaufjhWMGEyzJI1W1/XruPwd4pKou2nyt+r3n/zEwXFWb/AOgJM8DZlXVfmPeMI2ZJP8OLAVeWlU/S/I+YPuqOmcj938r3THyN+up82NGeRz1leTVwPuq6vBR7n8e8LOq+oP+eaI9g8eh1hv4apJnA38NvKd9ojkkyaeSfDzJd5Lcl+SYgf3en+TWdkHAc1vZdkm+luT2JHcleXMrvyDJ3a3uRgdNku1bG76bZGGSI1r5i9tz39Ye87nABcA+o+lVaLN6jO7bO+9Z844kz0oyr/2fzksyeWMftB0nxyQ5FdgDuDHJje2+R5J8tB2XNyfZrZUPJflCO5ZuTfLyVv6qgU/2C5PskGT3JN9qZXclOWQT2vbSJN9MsiDJ1wee/z3t7+L2JJ9OsjfwduD9o+lVPKFUlbcJvNFdp+m2dvtSK3s18NW2fg7dp5pV9T8FXEsX5C+kuw4UwOvo/qDT7vsq8ErgaOCKgf2fDuwM/IDVPcMd19O+HwPPGNj+b8BxbX0n4IfAU4FPAG9u5du0sucBt030v7G3DR6DjwBPa//XTwfeB5zT7vsKMLWtnwx8eR37vxVYPnAcv23gWD1mhOOogCMGjqmz2vpngVe09cnAPQPteHlb357ua/GnAx9sZVsAO4zw+n739zRwfH5nVXuAE4DpbX0psHVb37EtzwNOm+j/p/G+jcflKLRpflWbfhrly1W1Erh71ScaujB4HbDqek/bA1OAm4CLklxI9wdxU5ItgX8H/j7J1+iCY2O9Djgs7dLkdG/6k+n+uM5K8izgi1V1b9LreirajKrqF+1c/6nArwbuehnwl239aro37nX5fK3nNNE6/IbVx90C4M/a+muBFw4cO09LsgPwbeBjST5Dd3w9kORW4JPpfsz65aq6bSOf+wXAHwH/0J5nC7orJwAsAj6dZDbw5U14PU94niZ6Yvr1wHoGludX1X7t9ryqurKqfggcCNwJnJ/kQ1X1GN3VZb8AHAVcvwnPHeCogeeZXFU/rKqrgTe2ts1N8sqer1Gb36XAKXSXihnJWA0yrqj2sZuud7zqg+lTgJcNHF97VtUvq+oCutM1k4Cbkzy/qr5F1/v9KXB1kr/ayOcOcMfAc7y4qg5r970e+B90fx/z012S/0nBMHj8+yWww0bUuwE4Ocn2AEn2TLJrkj2AR6vq08BFwAGtztOrag5wGrApPZMb6D490p5n/7Z8blXdW1WXAV8DXrIJbdfjQFX9HJhJFwirfIfukjLQnU7551E+/MYeC98AftfDSLJfW+5dVXdW1YV01zZ7fuuFLqvuIpdXAgdsZFvuBvZMclB77K2T/FF749+rqv4ReD8wRHfZnCfFcWwYPP59BXjjqgHkkSpV1Tfozrf+73SX+JhFdwC/GPhuktuAD9Kd/9wB+Gq6S4J8k3UMHK7HucC26b5uuohuTAPg+CSL2vM8F/h0VT1I9+nqTgeQnzAuprt89CqnAm9rx8pJdNcWG43pwNdXDSCvx6nAcBuwvpvuCxQAp7VB4tvpTmN9nW4s4LYkC+nGxi7bmIZU1a+BY+hOO91Od2r1j+l6J59tr/V7wIVV9UtgNvCmNnD9BzuA7FdLJUn2DCRJhoEkCcNAkoRhIEnCMJAkYRhIkjAMJEnA/wcfrKUa6TS3rwAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1a1a4b8190>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Percent of Applicants who Purchase\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(member_pivot)),\n",
    "       member_pivot['Percent Purchase'].values,\n",
    "        color = ['#0070C0','#eb8f22'])\n",
    "ax.set_xticks(range(len(app_pivot)))\n",
    "ax.set_xticklabels(['Fitness Test', 'No Fitness Test'])\n",
    "ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])\n",
    "ax.set_yticklabels(['0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])\n",
    "plt.savefig('percent_apply_purchase.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x110a38c90>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Percent of Visitors who Purchase\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(final_member_pivot)),\n",
    "       final_member_pivot['Percent Purchase'].values,\n",
    "        color = ['#0070C0','#eb8f22'])\n",
    "ax.set_xticks(range(len(app_pivot)))\n",
    "ax.set_xticklabels(['Fitness Test', 'No Fitness Test'])\n",
    "ax.set_yticks([0, 0.05, 0.10, 0.15, 0.20])\n",
    "ax.set_yticklabels(['0%', '5%', '10%', '15%', '20%'])\n",
    "plt.savefig('percent_visitors_purchase.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
