class instagram:
    def __init__(self,name):
        self.name=name
        self.followers = 0
        self.following = 0

    def follow(self,user)  :
        self.following += 1
        user.followers += 1

praveen =  instagram("pavithra")
pavithra = instagram("praveen")

praveen.follow(pavithra)

print(praveen.following)
print(pavithra.followers)
