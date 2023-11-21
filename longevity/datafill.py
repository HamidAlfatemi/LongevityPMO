import os
import sys
import django

# Assuming your project root directory is C:\lpmo, adjust it if needed.
project_path = "C:/lpmo"
sys.path.append(project_path)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lpmo.settings')

# Initialize Django
django.setup()

# Import the Theory model after Django setup
from longevity.models import Theory

Theory.objects.all().delete() 
parent_theory1 = Theory.objects.create(theorytitle='Theories involving DNA', theorydesc='')

child_theory1 = Theory.objects.create(theorytitle='DNA damage (mutation)', theorydesc='', parent_t=parent_theory1)
child_theory = Theory.objects.create(theorytitle='Epigenetic modification', theorydesc='', parent_t=parent_theory1)
child_theory = Theory.objects.create(theorytitle='Nuclear DNA damage (mutation)', theorydesc='', parent_t=parent_theory1)
child_theory = Theory.objects.create(theorytitle='Mitochondrial DNA (mtDNA) damage', theorydesc='', parent_t=parent_theory1)
child_theory = Theory.objects.create(theorytitle='Telomere shortening', theorydesc='', parent_t=parent_theory1)
child_theory = Theory.objects.create(theorytitle='Transposable element activation', theorydesc='', parent_t=parent_theory1)

parent_theory2 = Theory.objects.create(theorytitle='Error catastrophe theories', theorydesc='')
child_theory = Theory.objects.create(theorytitle='Accumulation of Misfolded Proteins', theorydesc='', parent_t=parent_theory2)
child_theory = Theory.objects.create(theorytitle='Error-Prone DNA Repair', theorydesc='', parent_t=parent_theory2)

parent_theory3 = Theory.objects.create(theorytitle='Protein Homeostasis Theories', theorydesc='')
child_theory = Theory.objects.create(theorytitle='Protein Aggregation Theories', theorydesc='', parent_t=parent_theory3)
child_theory = Theory.objects.create(theorytitle='Chaperone Dysfunction Theories', theorydesc='', parent_t=parent_theory3)

parent_theory4 = Theory.objects.create(theorytitle='Accumulation theories', theorydesc='')
child_theory = Theory.objects.create(theorytitle='Lipofuscin accumulation', theorydesc='', parent_t=parent_theory4)
child_theory = Theory.objects.create(theorytitle='Cross-links accumulation', theorydesc='', parent_t=parent_theory4)
child_theory = Theory.objects.create(theorytitle='Misfolded protein aggregates', theorydesc='', parent_t=parent_theory4)
child_theory = Theory.objects.create(theorytitle='Giant mitochondria', theorydesc='', parent_t=parent_theory4)
child_theory = Theory.objects.create(theorytitle='Senescent cells accumulation', theorydesc='', parent_t=parent_theory4)

parent_theory5 = Theory.objects.create(theorytitle='Systemic signaling theories', theorydesc='')
child_theory = Theory.objects.create(theorytitle='Endocrine theory', theorydesc='', parent_t=parent_theory5)
child_theory = Theory.objects.create(theorytitle='Immune system dysfunction', theorydesc='', parent_t=parent_theory5)
child_theory = Theory.objects.create(theorytitle='Stem cells aging', theorydesc='', parent_t=parent_theory5)

parent_theory6 = Theory.objects.create(theorytitle='Environmental factors', theorydesc='')
child_theory = Theory.objects.create(theorytitle='Hazardous toxic material', theorydesc='', parent_t=parent_theory6)
child_theory = Theory.objects.create(theorytitle='Radiations', theorydesc='', parent_t=parent_theory6)
child_theory = Theory.objects.create(theorytitle='Germs: Bacteria, Viruses, Fungi, and Pro', theorydesc='', parent_t=parent_theory6)
child_theory = Theory.objects.create(theorytitle='Interventions', theorydesc='', parent_t=parent_theory6)
child_theory = Theory.objects.create(theorytitle='Traumatic Injuries', theorydesc='', parent_t=parent_theory6)

parent_theory7 = Theory.objects.create(theorytitle='Nutritional theories', theorydesc='')
parent_theory8 = Theory.objects.create(theorytitle='Oxidative stress and free radical', theorydesc='')
parent_theory9 = Theory.objects.create(theorytitle='Inflammaging', theorydesc='')
parent_theory10 = Theory.objects.create(theorytitle='Mitochondrial dysfunction', theorydesc='')
parent_theory11 = Theory.objects.create(theorytitle='Mitochondria deficiency', theorydesc='')
parent_theory12 = Theory.objects.create(theorytitle='Hormonal Theories', theorydesc='')
child_theory = Theory.objects.create(theorytitle='Insulin/IGF-1 Signaling Theory', theorydesc='', parent_t=parent_theory12)
child_theory = Theory.objects.create(theorytitle='Hypothalamic-Pituitary-Adrenal Axis', theorydesc='', parent_t=parent_theory12)

# Access the parent theory of a child theory parent_theory = child_theory.parent_t # Access the children theories of a parent theory children_theories = parent_theory.children.all() 
all_theories = Theory.objects.all()
for theory in all_theories:
    parent_t = theory.parent_t.theory_id if theory.parent_t else None
    print(f'{theory}: Parent ID: {parent_t}')