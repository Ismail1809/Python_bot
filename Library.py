class ReadableObj:
	def read(self):
		print("Reading..")
	def buy(self):
		print("Buying")
	def taking(self):
		print("Taking for a time")

class Book(readableObj):
	def Story(self):
		print("Reading story")

	def Poem(self):
		print("Reading poem")

	def fable(self):
		print("Reading fable")

class Enc(readableObj):
	def Animals(self):
		print("Reading about Animals body structure")

	def Dino(self):
		print("Reading about dinosaurs")

	def Human(self):
		print("Reading about Human body structure")

class Magazine(readableObj):
	def News(self):
		print("Reading news")

	def fashion(self):
		print("Appreciate new fashion")

	def Techno(self):
		print("Learn new gadgets and technologies")

class Voc(readableObj):
	def Translate1(self):
		print("Translate words from russia to english")

	def Translate2(self):
		print("Translate words from english to russia")

class User(readableObj):
	def Enter(self):
		print("Enter the library")

	def read_object(self, object_to_read):
		object_to_read.read()

class Librarian(readableObj):
	def Sell(self):
		print("Sell products")
	def Give(self):
		print("Give book")


if __name__ == "__main__":
	test_user = User()

	test_book = Book()

	test_user.read_object(test_book)