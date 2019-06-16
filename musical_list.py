musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]
# Your code
for artists in musical_groups:
	print(", ".join(artists))

for artists in musical_groups:
	if len(artists) == 3:
		print(", ".join(artists))

learning_todos = [
    "Go to local Python meetup",
    "Put study times on my calendar",
    "Check out what Python e-books are available from my library",
    "Research job openings for keywords",
]

learning_todos.insert(0, "Finish the Introducing Lists course")

print(learning_todos)

characters = [
    "T'Challa",
    "N'Jadaka",
    "Nakia",
    "Zuri",
    "Okoye",
    "Ramonda",
    "Shuri",
]

fave = characters[-1]
print(fave)


# .append(<value>) - Add a new value onto the end of a list.

# .extend(<iterable>) - Make a list longer by adding on the members of another iterable.

# .insert(<index>, <value>) - Add a value to a list at a particular index.

best = ["Tom", "Jim", "Mary"]
print(best)
best.append(["Wayne", "John"])
print(best)
best.extend("ab")
print(best)
best.insert(0, "start")
print(best)