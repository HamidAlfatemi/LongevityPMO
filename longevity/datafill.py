import os
import sys
import django

from django.db.models import F, IntegerField, Value
from django.db.models.functions import Length, Greatest
from django.db.models import Q
from django.db.models.functions import Cast
from django.db.models.fields import FloatField


# Assuming your project root directory is C:\lpmo, adjust it if needed.
project_path = "C:/lpmo"
sys.path.append(project_path)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lpmo.settings')

# Initialize Django
django.setup()

# Import the Theory model after Django setup
from longevity.models import Node # Theory

#Node.objects.filter(Q(container=5) & ~Q(nodeshape=7)).update(cyrend=10)
Node.objects.filter(Q(container=5)).update(cyrend=10)
Node.objects.filter(ref_num='803').update(cyrend=15)
Node.objects.filter(Q(container=6)).update(cyrend=30)
Node.objects.filter(ref_num='800').update(cyrend=35)
Node.objects.all().update(posnx=Cast(F('posx'), output_field=FloatField()) / 100.0)
Node.objects.all().update(posny=Cast(F('posy'), output_field=FloatField()) / 100.0)
#Node.objects.all().update(container=F('container') / 10)
# Node.objects.filter(nodeshape=4).update(container=12)
# Node.objects.filter(nodeshape=5).update(container=17)
# Node.objects.filter(container=1).update(parent_n_id=313)
# Node.objects.filter(container=2).update(parent_n_id=314)
# Node.objects.filter(container=3).update(parent_n_id=312)
# Node.objects.filter(container=4).update(parent_n_id=315)
# Node.objects.filter(container=5).update(parent_n_id=316)
# Node.objects.filter(container=6).update(parent_n_id=246)
# Node.objects.filter(container=7).update(parent_n_id=317)
# Node.objects.filter(container=8).update(parent_n_id=318)
# Node.objects.filter(container=9).update(parent_n_id=319)
# Node.objects.filter(container=10).update(parent_n_id=320)
# Node.objects.filter(container=11).update(parent_n_id=321)
# Node.objects.filter(container=12).update(parent_n_id=322)
# Node.objects.filter(container=13).update(parent_n_id=323)
# Node.objects.filter(container=14).update(parent_n_id=324)
# Node.objects.filter(container=15).update(parent_n_id=325)
# Node.objects.filter(container=16).update(parent_n_id=326)
# Node.objects.filter(container=17).update(parent_n_id=327)

# Node.objects.update(width = Greatest(Length('nodecaption') * 2.5, Value(130)))
# Node.objects.update(height = Greatest(Length('nodecaption') * .5, Value(130)))
# Node.objects.update(posx = 0)
# Node.objects.update(posy = 0)

# # Node.objects.update(width=Func(Length('nodecaption') * 2, Value(130), function='LEAST', output_field=IntegerField()))
# # Node.objects.update(height=Func(Length('nodecaption') * 0.25, Value(130), function='LEAST', output_field=IntegerField()))

# Node.objects.filter(ref_num='900').update(width=8545, height=1284, posx=4593, posy=5598)
# Node.objects.filter(ref_num='801').update(width=8545, height=1147, posx=4593, posy=4315)
# Node.objects.filter(ref_num='200').update(width=2596, height=3009, posx=7652, posy=2189)
# Node.objects.filter(ref_num='802').update(width=5657, height=2836, posx=3526, posy=2102)
# Node.objects.filter(ref_num='803').update(width=1444, height=929, posx=1797, posy=1199)
# Node.objects.filter(ref_num='800').update(width=663, height=686, posx=4134, posy=1077)
# Node.objects.filter(ref_num='804').update(width=1683, height=1139, posx=5328, posy=1304)
# Node.objects.filter(ref_num='805').update(width=2205, height=1771, posx=1988, posy=2581)
# Node.objects.filter(ref_num='806').update(width=480, height=346, posx=5238, posy=2157)
# Node.objects.filter(ref_num='807').update(width=3079, height=365, posx=4725, posy=3480)
# Node.objects.filter(ref_num='808').update(width=224, height=266, posx=6373, posy=3762)
# Node.objects.filter(ref_num='809').update(width=400, height=5281, posx=9175, posy=3325)
# Node.objects.filter(ref_num='810').update(width=242, height=173, posx=5338, posy=2293)
# Node.objects.filter(ref_num='811').update(width=231, height=1391, posx=3070, posy=2726)
# Node.objects.filter(ref_num='812').update(width=161, height=133, posx=4493, posy=1567)
# Node.objects.filter(ref_num='813').update(width=267, height=855, posx=2502, posy=1217)
# Node.objects.filter(ref_num='814').update(width=934, height=5556, posx=500, posy=3462)

# contrefnum = ['900', '801', '200', '802', '803', '800', '804', '805', '806', '807', '808', '809', '810', '811', '812', '813', '814']
    
# # for crefnum in contrefnum:
    # # nodes = Node.objects.filter(ref_num=crefnum)
    # # for node in nodes:
        # # node.width = int(node.width * 0.5)
        # # node.height = int(node.height * 0.5)
        # # node.posx = int(node.posx * 0.5)
        # # node.posy = int(node.posy * 0.5)
        # # node.save()

# for crefnum in contrefnum:
    # container_record = Node.objects.get(ref_num = crefnum)
    # positionx = container_record.posx - container_record.width/2 + 80
    # positiony = container_record.posy - container_record.height/2 + 80
    # containerw = container_record.width
    # containerh = container_record.height
    # containerid = container_record.node_id
    # containerx = container_record.posx
    # containery = container_record.posy
# #    node_records = Node.objects.filter(parent_n_id = containerid)
    # node_records = Node.objects.filter(Q(parent_n_id=containerid) & ~Q(nodeshape=7))
    # for nodrecord in node_records:
        # if positionx + 80 + nodrecord.width > containerx + containerw / 2:
           # positionx = containerx - containerw / 2 + nodrecord.width / 2 + 80
           # positiony = positiony + nodrecord.height/2 + 210
        
        # nodrecord.posx=positionx
        # nodrecord.posy=positiony
        # nodrecord.save()
        # positionx = positionx + nodrecord.width + 80

# # nodes = Node.objects.all()
# # for node in nodes:
    # # node.width = int(node.width * 0.5)
    # # node.height = int(node.height * 0.5)
    # # node.posx = int(node.posx * 0.5)
    # # node.posy = int(node.posy * 0.5)
    # # node.save()

    # # if crefnum == '802': # Cytosolic Compartment of the Cell
        # # cellmembright = ['077', '078', '079', '082', '085', '095', '163', '096']
        # # positionx = containerx + containerw
        # # positiony = containery + 80
        # # for nodrefnum in cellmembright:
            # # node_record = Node.objects.get(ref_num = nodrefnum)
            # # node_record.posx = containerx + containerw - node_record.width / 2
            # # node_record.posy = positiony
            # # node_record.save()
            # # positiony = positiony + node_record.height + 80
        # # cellmembbelow = ['076', '089', '091', '093']
        # # positionx = containerx + 80
        # # for nodrefnum in cellmembbelow:
            # # node_record = Node.objects.get(ref_num = nodrefnum)
            # # positiony = containery + containerh - node_record.height / 2
            # # node_record.posx = positionx
            # # node_record.posy = positiony
            # # node_record.save()
            # # positionx = positionx + node_record.width + 80
        # # cellmembleft = ['739', '016']
        # # positiony = containery + 80
        # # for nodrefnum in cellmembleft:
            # # node_record = Node.objects.get(ref_num = nodrefnum)
            # # node_record.posx = containerx - node_record.width / 2
            # # node_record.posy = positiony
            # # node_record.save()
            # # positiony = positiony + node_record.height + 80
    # # if crefnum == '200': # Extracellular Spaces: ECM, Blood Plasma, Lymph, CSF
        # # cellmembleft = ['232', '234']
        # # positiony = containery + containerh
        # # for nodrefnum in cellmembleft:
            # # node_record = Node.objects.get(ref_num = nodrefnum)
            # # positionx = containerx - node_record.width / 2
            # # positiony = positiony - node_record.height - 80
            # # node_record.posx = positionx
            # # node_record.posy = positiony
            # # node_record.save()
    # # if crefnum == '803': # Lysosome – Hydrolysis - for recycling. Accumulation in nonmitotic cells
        # # cellmembright = ['005', '007', '009', '010']
        # # positiony = containery + 80
        # # for nodrefnum in cellmembright:
            # # node_record = Node.objects.get(ref_num = nodrefnum)
            # # positionx = containerx - node_record.width / 2
            # # node_record.posx = positionx
            # # node_record.posy = positiony
            # # node_record.save()
            # # positiony = positiony + node_record.height + 80
    # # if crefnum == '804': # Mitochondria in nonmitotic cell
        # # cellmembleft = ['416']
        # # positiony = containery + containerh
        # # for nodrefnum in cellmembleft:
            # # node_record = Node.objects.get(ref_num = nodrefnum)
            # # positionx = containerx - node_record.width / 2
            # # positiony = positiony - node_record.height - 80
            # # node_record.posx = positionx
            # # node_record.posy = positiony
            # # node_record.save()
    # # if crefnum == '805': # Cell Nucleus – Genetics
        # # cellmembright = ['355', '034', '356', '301']
        # # positiony = containery + 80
        # # for nodrefnum in cellmembright:
            # # node_record = Node.objects.get(ref_num = nodrefnum)
            # # positionx = containerx + containerw - node_record.width / 2
            # # node_record.posx = positionx
            # # node_record.posy = positiony
            # # positiony = positiony + node_record.height + 80
            # # node_record.save()
    # # if crefnum == '806': # Endoplasmic Reticulum
        # # cellmembbelow = ['097']
        # # positiony = containery + containerh
        # # for nodrefnum in cellmembbelow:
            # # node_record = Node.objects.get(ref_num = nodrefnum)
            # # positionx = containerx + containerw - node_record.width - 80
            # # node_record.posx = positionx
            # # node_record.posy = positiony - node_record.height / 2
            # # node_record.save()
            
# # Theory.objects.all().delete() 
# # parent_theory1 = Theory.objects.create(theorytitle='Theories involving DNA', theorydesc='')

# # child_theory1 = Theory.objects.create(theorytitle='DNA damage (mutation)', theorydesc='', parent_t=parent_theory1)
# # child_theory = Theory.objects.create(theorytitle='Epigenetic modification', theorydesc='', parent_t=parent_theory1)
# # child_theory = Theory.objects.create(theorytitle='Nuclear DNA damage (mutation)', theorydesc='', parent_t=parent_theory1)
# # child_theory = Theory.objects.create(theorytitle='Mitochondrial DNA (mtDNA) damage', theorydesc='', parent_t=parent_theory1)
# # child_theory = Theory.objects.create(theorytitle='Telomere shortening', theorydesc='', parent_t=parent_theory1)
# # child_theory = Theory.objects.create(theorytitle='Transposable element activation', theorydesc='', parent_t=parent_theory1)

# # parent_theory2 = Theory.objects.create(theorytitle='Error catastrophe theories', theorydesc='')
# # child_theory = Theory.objects.create(theorytitle='Accumulation of Misfolded Proteins', theorydesc='', parent_t=parent_theory2)
# # child_theory = Theory.objects.create(theorytitle='Error-Prone DNA Repair', theorydesc='', parent_t=parent_theory2)

# # parent_theory3 = Theory.objects.create(theorytitle='Protein Homeostasis Theories', theorydesc='')
# # child_theory = Theory.objects.create(theorytitle='Protein Aggregation Theories', theorydesc='', parent_t=parent_theory3)
# # child_theory = Theory.objects.create(theorytitle='Chaperone Dysfunction Theories', theorydesc='', parent_t=parent_theory3)

# # parent_theory4 = Theory.objects.create(theorytitle='Accumulation theories', theorydesc='')
# # child_theory = Theory.objects.create(theorytitle='Lipofuscin accumulation', theorydesc='', parent_t=parent_theory4)
# # child_theory = Theory.objects.create(theorytitle='Cross-links accumulation', theorydesc='', parent_t=parent_theory4)
# # child_theory = Theory.objects.create(theorytitle='Misfolded protein aggregates', theorydesc='', parent_t=parent_theory4)
# # child_theory = Theory.objects.create(theorytitle='Giant mitochondria', theorydesc='', parent_t=parent_theory4)
# # child_theory = Theory.objects.create(theorytitle='Senescent cells accumulation', theorydesc='', parent_t=parent_theory4)

# # parent_theory5 = Theory.objects.create(theorytitle='Systemic signaling theories', theorydesc='')
# # child_theory = Theory.objects.create(theorytitle='Endocrine theory', theorydesc='', parent_t=parent_theory5)
# # child_theory = Theory.objects.create(theorytitle='Immune system dysfunction', theorydesc='', parent_t=parent_theory5)
# # child_theory = Theory.objects.create(theorytitle='Stem cells aging', theorydesc='', parent_t=parent_theory5)

# # parent_theory6 = Theory.objects.create(theorytitle='Environmental factors', theorydesc='')
# # child_theory = Theory.objects.create(theorytitle='Hazardous toxic material', theorydesc='', parent_t=parent_theory6)
# # child_theory = Theory.objects.create(theorytitle='Radiations', theorydesc='', parent_t=parent_theory6)
# # child_theory = Theory.objects.create(theorytitle='Germs: Bacteria, Viruses, Fungi, and Pro', theorydesc='', parent_t=parent_theory6)
# # child_theory = Theory.objects.create(theorytitle='Interventions', theorydesc='', parent_t=parent_theory6)
# # child_theory = Theory.objects.create(theorytitle='Traumatic Injuries', theorydesc='', parent_t=parent_theory6)

# # parent_theory7 = Theory.objects.create(theorytitle='Nutritional theories', theorydesc='')
# # parent_theory8 = Theory.objects.create(theorytitle='Oxidative stress and free radical', theorydesc='')
# # parent_theory9 = Theory.objects.create(theorytitle='Inflammaging', theorydesc='')
# # parent_theory10 = Theory.objects.create(theorytitle='Mitochondrial dysfunction', theorydesc='')
# # parent_theory11 = Theory.objects.create(theorytitle='Mitochondria deficiency', theorydesc='')
# # parent_theory12 = Theory.objects.create(theorytitle='Hormonal Theories', theorydesc='')
# # child_theory = Theory.objects.create(theorytitle='Insulin/IGF-1 Signaling Theory', theorydesc='', parent_t=parent_theory12)
# # child_theory = Theory.objects.create(theorytitle='Hypothalamic-Pituitary-Adrenal Axis', theorydesc='', parent_t=parent_theory12)


# # Access the parent theory of a child theory parent_theory = child_theory.parent_t # Access the children theories of a parent theory children_theories = parent_theory.children.all() 
# # all_theories = Theory.objects.all()
# # for theory in all_theories:
    # # parent_t = theory.parent_t.theory_id if theory.parent_t else None
    # # print(f'{theory}: Parent ID: {parent_t}')