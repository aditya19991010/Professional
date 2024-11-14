# https://biopython.org/DIST/docs/tutorial/Tutorial.html
# https://biopython.org/


from Bio.Seq import Seq
from Bio import SeqIO



def main():

    # Currently, Biopython has code to extract information from the following databases:
    #
    # Entrez (and PubMed) from the NCBI – See Chapter ‍9.
    # ExPASy – See Chapter ‍10.
    # SCOP – See the Bio.SCOP.search() function.

    ### Sequence objects
    # we can deal with Seq objects as if they were normal Python strings, for example
    # getting the length, or iterating over the elements:
    my_seq = Seq("GATCG")
    for index, letter in enumerate(my_seq):
        print("Index Value = ", index, "Value = ", letter)

    print(my_seq[0], my_seq[1])
    # non-overlapping count
    new_seq = Seq("AAAATTCCGGAAA")
    print(new_seq.count("AA"))
    my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
    print(len(my_seq))
    print(my_seq.count("G"))

    # GC fraction
    from Bio.SeqUtils import gc_fraction
    my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
    gc_f = (my_seq.count("G") + my_seq.count("C")) / len(my_seq) * 100
    print(gc_f)
    print("GC fraction =", gc_fraction(my_seq))

    # Note that using the Bio.SeqUtils.gc_fraction() function should automatically cope with mixed case
    # sequences and the ambiguous nucleotide S which means G or C.
    my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGCSSS")
    print("GC fraction with S = ", gc_fraction(my_seq))

    ### slicing a sequence - similar to strings
    my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
    print("Slice 4th position to 11th pos ", my_seq[4:12])
    print("Slice starting from 0 every third character", my_seq[0::3])
    print("Slice Starting from 1 every third character", my_seq[1::3])
    print("Reverse ", my_seq[::-1])

    ### Turning Seq objects into strings
    # If you really do just need a plain string, for example to write to a file, or insert into a database,
    # then this is very easy to get:
    print("Seq is converted to string", str(my_seq))

    ### Concatenating or adding sequences
    seq1 = Seq("ACGT")
    seq2 = Seq("AACCGG")
    print("Concatenated string", seq1 + seq2)

    # Biopython does not check the sequence contents and will not raise an exception
    # if for example you concatenate a protein sequence and a DNA sequence (which is likely a mistake):
    protein_seq = Seq("EVRNAK")
    dna_seq = Seq("ACGT")
    print("Protein and DNA seq", protein_seq + dna_seq)

    # You may often have many sequences to add together, which can be done with a for loop like this:
    list_of_seqs = [Seq("ACGT"), Seq("AACC"), Seq("GGTT")]
    concatenated = Seq("")
    for s in list_of_seqs:
        concatenated += s
    print("concatenated seq", concatenated)

    # Like Python strings, Biopython Seq also has a .join method
    contigs = [Seq("ATG"), Seq("ATCCCG"), Seq("TTGCA")]
    spacer = Seq("N" * 10)
    print("join illustration", spacer.join(contigs))

    # Nucleotide sequences and (reverse) complements
    my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
    print("seq complement", my_seq.complement())
    print("reverse complement", my_seq.reverse_complement())

    # Transcription
    coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
    template_dna = coding_dna.reverse_complement()
    print("coding dna", coding_dna)
    print("templa dna", template_dna)
    messenger_rna = coding_dna.transcribe()
    print("coding    dna", coding_dna)
    print("messenger rna", messenger_rna)
    # back_transcription
    messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
    print("messenger   rna", messenger_rna)
    print("back_transcribe", messenger_rna.back_transcribe())

    # Translation
    messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
    print("translated from mRNA", messenger_rna.translate())
    # You can also translate directly from the coding strand DNA sequence:
    coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
    print("translated from coding dna", coding_dna.translate())

    ### SeqIO object
    allSeqRecords = []
    allSeqIDs = []
    pathToFile = "ls_orchid.fasta"
    for seq_record in SeqIO.parse(pathToFile, "fasta"):
        allSeqRecords.append(seq_record)
        allSeqIDs.append(seq_record.id.split("|")[1])
        print(seq_record.id)
        print(str(seq_record.seq))
        print(len(seq_record))

    ## print out fun stuff about the sequences
    print("We found ", len(allSeqIDs), "sequences")
    print("information on the third sequence:")
    ind = 2
    seqRec = allSeqRecords[ind]
    print("\t", "GI number     ", allSeqIDs[ind])
    print("\t", "full id       ", seqRec.id)
    print("\t", "num nucleo.   ", len(seqRec.seq))
    print("\t", "1st 10 nucleo.", seqRec.seq[:10])

    for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"):
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(len(seq_record))


    ### entrez databases
    # ***IMPORTANT***
    # Before using Biopython to access the NCBI’s online resources (via Bio.Entrez or some of the other modules),
    # please read the NCBI’s Entrez User Requirements. If the NCBI finds you are abusing their systems,
    # they can and will ban your access!
    #
    # To paraphrase: For any series of more than 100 requests, do this at weekends or outside USA peak times.
    # This is up to you to obey. Use the http://eutils.ncbi.nlm.nih.gov address, not the standard NCBI Web address.
    # Biopython uses this web address. Make no more than three requests every seconds (relaxed from at most one
    # request every three seconds in early 2009). This is automatically enforced by Biopython. Use the optional
    # email parameter so the NCBI can contact you if there is a problem. You can either explicitly set this as
    # a parameter with each call to Entrez (e.g. include email=”A.N.Other@example.com” in the argument list),
    # or as of Biopython 1.48, you can set a global email address:

    # credit: https://biopython.org/docs/1.75/api/Bio.Entrez.html#module-Bio.Entrez
    # credit: https://people.duke.edu/~ccc14/pcfb/biopython/BiopythonEntrez.html

    from Bio import Entrez
    # Please DO NOT use a random email. it’s better not to give an email at all. The email parameter will be
    # mandatory from June 1, 2010.
    Entrez.email = "shyam@ibab.ac.in"


    # What databases do I have access to?
    # einfo Provides field index term counts, last update, and available links for each database.
    handle = Entrez.einfo()
    # read Parses the XML results returned by any of the above functions.
    record = Entrez.read(handle)
    print("I have access to the following databases", record["DbList"])
    handle.close()


    # What if I want info about a database?
    handle = Entrez.einfo(db="pubmed")
    record = Entrez.read(handle)
    print("DBInfo Description", record["DbInfo"]["Description"])
    print("DBInfo count", record["DbInfo"]["Count"])
    handle.close()


    # How do I search a db for a given term?
    handle = Entrez.esearch(db="pubmed", term="autism machine learning")
    record = Entrez.read(handle)
    print("search results, record idlist", record["IdList"])
    handle.close()

    # Other databases?
    handle = Entrez.esearch(db="nucleotide", term="Cypripedioideae[Orgn] AND matK[Gene]")
    record = Entrez.read(handle)
    print("Count", record["Count"])
    handle.close()

    # Get all books that have ‘computational’ as a term
    handle = Entrez.esearch(db="books", term="computational")
    record = Entrez.read(handle)
    print("Count of books", record["Count"])
    print("books id list", record["IdList"])
    handle.close()

    # retrieve an individual item
    handle = Entrez.efetch(db="nucleotide", id="186972394", rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    print("item details")
    print(record)

    # retrieve another item
    handle = Entrez.efetch(db="pubmed", id="37920379")
    print("Pubmed article info")
    print(handle.read())

    print('End')

# credit: # https://learning.rc.virginia.edu/notes/biopython/
def biopython_exercises():

    # ### find the protein records associated with the human Pax6 gene and download the associated sequences in FASTA format.
    # from Bio import Entrez
    #
    # Entrez.email = "shyam@ibab.ac.in"  # your email address is required
    # handle = Entrez.esearch(db="protein", term=["Homo sapiens[Orgn] AND pax6[Gene]"], usehistory="y")
    # record = Entrez.read(handle)
    # handle.close()
    # # iterate over items
    # for k, v in record.items():
    #     print(k, v)
    #
    # # # fetch records using id list
    # Entrez.email = "shyam@ibab.ac.in"  # your email address is required
    # handle = Entrez.efetch(db="protein", rettype="fasta", retmode="text", id=record["IdList"])
    # result = handle.read()  # return type is simple string
    # handle.close()
    # # remove empty lines
    # fastaseq = result.replace("\n\n","\n")
    # with open('HsPax6-protein.fasta', 'w') as f:
    #    f.write(fastaseq)
    #
    #
    # ### retrieve the nucleotide sequences of top 5 ID hits as GenBank files.
    # Entrez.email = "shyam@ibab.ac.in"  # your email address is required
    # handle = Entrez.esearch(db="nucleotide", term=["Homo sapiens[Orgn] AND pax6[Gene]"], retmax=5, usehistory="y")
    # record = Entrez.read(handle)
    # handle.close()
    # for k, v in record.items():
    #     print(k, v)
    #
    # # iterate over ids in list
    # for seq_id in record["IdList"]:
    #     # get entry from Entrez
    #     print(seq_id)
    #     handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="gb", retmode="text")
    #     result = handle.read()
    #     handle.close()
    #     # save
    #     filename = f"HsPax6-{seq_id}-nucleotide.gb"
    #     print("Saving to file:", filename)
    #     with open(filename, 'w') as gbfile:
    #         # append fasta entry
    #         gbfile.write(result.rstrip() + "\n")
    #
    #
    # ### Find and download the top 10 FASTA EST nucleotide sequences for the mouse (Mus Musculus) TP53 tumor suppressor.
    # # Hint: look up the EST database descriptor in this table -
    # # https://www.ncbi.nlm.nih.gov/books/NBK25497/table/chapter2.T._entrez_unique_identifiers_ui/?report=objectonly
    # Entrez.email = "shyam@ibab.ac.in"  # your email address is required
    # handle = Entrez.esearch(db="nucest", term=["Mus musculus[Orgn] AND tp53[Gene]"], retmax=10, usehistory="y")
    # record = Entrez.read(handle)
    # handle.close()
    # for k, v in record.items():
    #     print(k, v)
    #
    # # iterate over ids in list
    # for seq_id in record["IdList"]:
    #     # get entry from Entrez
    #     print(seq_id)
    #     handle = Entrez.efetch(db="nucest", id=seq_id, rettype="fasta", retmode="text")
    #     result = handle.read()
    #     handle.close()
    #     # save
    #     filename = f"MmP53-{seq_id}-est.fasta"
    #     print("Saving to file:", filename)
    #     with open(filename, 'w') as fastafile:
    #         # append fasta entry
    #         fastafile.write(result.rstrip() + "\n")


    # ### Retrieve Protein Records from the ExPASy Database
    # # Here are a few examples demonstrating how to access the ExPASy databases Swissport and Prosite.
    # from Bio import ExPASy
    # from Bio import SwissProt
    #
    # # get single protein record
    # accession_no = "O23729"
    # handle = ExPASy.get_sprot_raw(accession_no)
    # record = SwissProt.read(handle)
    # print(record.entry_name)
    # print(record.sequence_length)
    # print(record.data_class)
    # print(record.accessions)
    # print(record.organism)
    # # print first 10 aa
    # print(record.sequence[:10])  # string

    print('End')


# Construct to not include whole program in other includes
if __name__ == "__main__":
   # main()
   biopython_exercises()