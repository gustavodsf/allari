# allari

> python version should be greater than 3.7, because I'm using dataclass lib.

#### Run the project

> To run the project you should use the following command

```py
python main.py --person 1
```

#### Run the test

> To run the test you should use the following command:

```py
python3 -m unittest discover -s test/ -p '*_test.py'
```

#### Folder structure
```
├── data
│   ├── contacts.json  # json with contacts data
│   └── persons.json   # json with persons data
├── src
│   ├── contact.py      # model that represents the contact of a person
│   ├── experience.py   # model that represents the experience of a person
│   ├── input_file.py    # class to read the json file and convert it to objects
│   ├── person.py       # model that represents a person
│   ├── phone.py        # model that represents the phone of a person
│   └── relationship.py # class to check if a person worked with another or is connected by phones 
├── test/
│   ├── 
│   └── 
├── main.py # capture the argument and call the other functions
└── README
```