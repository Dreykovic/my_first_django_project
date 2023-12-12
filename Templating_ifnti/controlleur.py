from posixpath import abspath
from jinja2 import Environment

from latex import build_pdf
from os.path import dirname, abspath


def generate_pdf(context):
    """INSTACIATION D'UN NOUVEL ENVIRONNEMENT AVEC DES OPTIONS DE BALISES PERSONNALISÉES"""
    j2_env = Environment(
        variable_start_string="\VAR{",
        variable_end_string="}",
        block_start_string="\BLOCK{",
        block_end_string="}",
        comment_start_string="\COMMENT{",
        comment_end_string="}",
    )
    """DECLARATION DE FICHIER"""
    #Fichier à lire contenant le template avec les balises
    fichier_in = open(dirname(abspath(__file__))+"/ifnti/liste_eleves.tex","r")
    
    #Fichier en sortie accueillant les données fournies
    fichier_out = open(dirname(abspath(__file__))+"/out/template_out.tex","w")
    
    template = fichier_in.read()#Lecture du template
    monContext = context
    monContext["image_path"] = dirname(abspath(__file__))+"/out/images/"
    
    """APPLICATION DE L'ENVIRONNEMENT ÉDITÉ SUR LE TEMPLATE"""
    j2_tamplate = j2_env.from_string(template)
    
    #Écriture dans le fichier en sortie
    fichier_out.write(j2_tamplate.render(monContext))
    fichier_out.close()
    
    mon_pdf = build_pdf(open(dirname(abspath(__file__))+"/out/template_out.tex","r"))
    mon_pdf.save_to(dirname(abspath(__file__))+"/out/liste_eleves.pdf")
    """FERMETURE DE CANAUX"""
    fichier_in.close()
    
monContext = {'eleves': [{"id":"12","nom": "audrey","prenom":"audrey","sexe":"M","date_naissance":"18/11/2001"},{"id":"12","nom": "audrey","prenom":"audrey","sexe":"M","date_naissance":"18/11/2001"},{"id":"12","nom": "audrey","prenom":"audrey","sexe":"M","date_naissance":"18/11/2001"}]}
generate_pdf(monContext)
