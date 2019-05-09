from app import db
from models import Post

#creating the database and the db tables
db.create_all()

#insert data
db.session.add(Post("A Beautiful Day", "Today was a really great day I had a lot of fun but now I'm honestly really tired and want to go to bed."))
db.session.add(Post("Ugh", "I want to be done with finals ugh when will it be summer and hot again so I don't have to worry about wearing a jacket."))
db.session.add(Post("Omg", "Wow I just realized I only have one year of college left. Time flies by so quickly I don't want it to end!!"))

#commit the changes
db.session.commit()
