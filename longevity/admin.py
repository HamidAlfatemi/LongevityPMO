from django.contrib import admin

# Register your models here.
from .models import Theory
admin.site.register(Theory)
from .models import Node
admin.site.register(Node)
from .models import Edge
admin.site.register(Edge)
from .models import Intervention
admin.site.register(Intervention)
from .models import NodeIntervention
admin.site.register(NodeIntervention)
from .models import StrategyIntervention
admin.site.register(StrategyIntervention)
from .models import InterventionStrategy
admin.site.register(InterventionStrategy)
from .models import InterventionTarget
admin.site.register(InterventionTarget)
from .models import Target
admin.site.register(Target)
from .models import Hallmark
admin.site.register(Hallmark)
from .models import NodeHallmark
admin.site.register(NodeHallmark)
#from .models import Intalternative
#admin.site.register(Intalternative)
from .models import Literature
admin.site.register(Literature)
from .models import InterventionLiterature
admin.site.register(InterventionLiterature)
from .models import Ddstep
admin.site.register(Ddstep)
from .models import Drawback
admin.site.register(Drawback)
from .models import Drawbacktype
admin.site.register(Drawbacktype)
# from .models import NodeGene
# admin.site.register(NodeGene)
from .models import Gene
admin.site.register(Gene)
from .models import InterventionGene
admin.site.register(InterventionGene)
from .models import Project
admin.site.register(Project)
from .models import ProjectIntervention
admin.site.register(ProjectIntervention)
from .models import TargetArticle
admin.site.register(TargetArticle)
from .models import NodeLiterature
admin.site.register(NodeLiterature)
from .models import SAE
admin.site.register(SAE)
from .models import Sbpathway
admin.site.register(Sbpathway)
from .models import SbpathwayTarget
admin.site.register(SbpathwayTarget)
from .models import NodeSbpathway
admin.site.register(NodeSbpathway)
from .models import InterventionSbp
admin.site.register(InterventionSbp)
from .models import Species
admin.site.register(Species)
from .models import Treatment
admin.site.register(Treatment)
from .models import InterventionTreatment
admin.site.register(InterventionTreatment)
from .models import Convenience
admin.site.register(Convenience)
from .models import ConvTre
admin.site.register(ConvTre)
from .models import Organization
admin.site.register(Organization)
from .models import Condition
admin.site.register(Condition)
from .models import isaecond
admin.site.register(isaecond)
from .models import InterventionSAE
admin.site.register(InterventionSAE)
from .models import DoseUnit
admin.site.register(DoseUnit)
from .models import ISAELiterature
admin.site.register(ISAELiterature)
from .models import Subject
admin.site.register(Subject)
from .models import ProjectSubject
admin.site.register(ProjectSubject)
from .models import InterventionDrawback
admin.site.register(InterventionDrawback)
from .models import StrategyDrawback
admin.site.register(StrategyDrawback)
from .models import GeneSpecies
admin.site.register(GeneSpecies)
from .models import GeneSet
admin.site.register(GeneSet)
from .models import gsgene
admin.site.register(gsgene)
from .models import nodegs
admin.site.register(nodegs)
