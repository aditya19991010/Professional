'''Create a class called MicroOrganism() inherited by two subclasses
Virus(MicroOrganism) and Bacteria(MicroOrganism).
Have methods inside these sub classes called replicate() which should print “Replicates by fission”
for bacteria and “Replicates inside host cell” for virus.
The parent class replicate should raise an error message “Not implemented”
From a function replicate_organism(Microorganism), call organism.replicate()
In main, create a virus object and call replicate(organism) and bacteria object
and call replicate(organism). Observe the output.'''


class MicroOrganism():
    try:
        def replicate(self):
            raise NotImplementedError("Not implemented")
    except NotImplementedError:
        print("Not implemented")

class Virus(MicroOrganism):
    def replicate(self):
        print("Replicates inside host cell")

class Bacteria(MicroOrganism):
    def replicate(self):
        print("Replicates by fission")

def replicate_organism(organism):
    organism.replicate()


def main():
    v = Virus()
    b = Bacteria()
    m = MicroOrganism()
    replicate_organism(v)
    replicate_organism(b)
    replicate_organism(m)


if __name__=="__main__":
    main()