import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem

from rdkit import RDLogger
RDLogger.DisableLog('rdApp.*')

import numpy as np
import random 
import copy

from pysoftk.linear_polymer import linear_polymer as lp
from pysoftk.linear_polymer import super_monomer  as sm

from .utils import *
from pysoftk.linear_polymer.utils import *

class Rnp():
    """
    A class for creating a random copolymer 
    from given RDKit molecules.

    Attributes:
    -----------
    ma           Molecular core to be decorated
    mb           Molecular branches to be added to the core
    atom         A place-holder atom to connect the molecules 
 

    Examples
    ---------

    Note:
    -----
    RDKit package must be installed.
    """
    
    __slots__ = 'ma', 'mb', 'atom'

    def __init__(self, ma, mb, atom):
       """
       Initialize this class.
          
       Parameters
       ----------
       ma : rdkit.Chem.rdchem.Mol
            RDKit Mol object

       mb : rdkit.Chem.rdchem.Mol
            RDKit Mol object
 
       atom : str
            The placeholder atom to combine the molecules 
            and form a new monomer

       """
       
       self.ma = ma
       self.mb = mb
       self.atom = atom

    def random_ab_copolymer(self, len_polymer, pA,
                            iter_ff=100, FF="MMFF"):
       """ 
       Function to build a random copolymer using an user 
       provided probability (pA) for merging the monomer 
       ma and imposiing the condition pB=1-pA.


       Parameters
       -----------

       len_polymer: int
          User defined length of the polymer.

       pA: float
          User defined attaching probability of
           ma.

       iter_ff: int
           User defined iterations for a FF.

       FF: str
           User selected FF between "MMFF" or "UFF".      
 
       Return:
       -------    
       mol: rdkit.Chem.rdchem.Mol
          RDKit Mol object
        
       """

       ma=self.ma
       mb=self.mb
       atom=self.atom

       rand = np.random.rand()
    
       if rand<pA:
          m1 = ma
       else:
          m1 = mb
    
       rand = np.random.rand()
    
       if rand<pA:
          m2 = ma
       else:
          m2 = mb
        
       monomer = sm.Sm(m1, m2, str(atom))    
    
       for i in range(len_polymer-1):
        
          rand = np.random.rand()
    
          if rand<pA:
              m3 = ma
          else:
              m3 = mb
            
          monomer=sm.Sm(monomer.mon_to_poly(), m3, str(atom))
        
       mol=monomer.mon_to_poly()
       newMol_H=swap_hyd(mol, iter_ff, str(atom), FF)
    
       return newMol_H
    
    def random_abc_copolymer(self, mC, len_polymer, pA,
                             pB, iter_ff=100, FF="MMFF"):
        
       """ 
       Function to build a random copolymer based on  
       an user defined probability (pA) of merging mA, 
       pB for monomer mb, and the condition pC=1-pA-pB.

       Parameters
       -----------
       mc: rdkit.Chem.rdchem.Mol
           RDKit Mol object #

       len_polymer: float
           User defined length of the polymer.

       pA: float
           User defined attaching probability of
           ma.

       pB: float
           User defined attaching porbability of
           mb.

       atom: str
           User defined atom used as place-holder.

       iter_ff: int
           User defined iterations for a FF.#

       FF: str
           User selected FF.      
 
       Return:
       -------
    
       mol: rdkit.Chem.rdchem.Mol
             RDKit Mol object

       """

       ma=self.ma
       mb=self.mb
       atom=self.atom
    
       rand = np.random.rand()
       pAB=pA+pB
    
       if rand<pA:
         m1 = ma

       elif rand<pAB:
         m1 = mb

       else:
         m1 = mc
    
       rand = np.random.rand()
    
       if rand<pA:
           m2 = ma

       elif rand<pAB:
           m2 = mb

       else: 
           m2 = mc
        
       monomer = sm.Sm(m1, m2, str(atom))
    
       for i in range(len_polymer-1):
          rand = np.random.rand()
    
          if rand<pA:
              m3 = ma

          elif rand<pAB:
              m3 = mb#

          else:
              m3 = mc

          monomer=sm.Sm(monomer.mon_to_poly(), m3, str(atom))
       
       mol = monomer.mon_to_poly()
       newMol_H=swap_hyd(mol, iter_ff, str(atom), FF)
    
       return newMol_H

#if __name__ == "__main__":
