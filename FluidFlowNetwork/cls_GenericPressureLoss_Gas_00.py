# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 19:06:11 2023

@author: zeta_plusplus
"""

class GenericPressureLoss_Gas_00:
    p1: float() = 100*1000
    T1: float() = 288.15
    
    p2: float() = 100*1000
    T2: float() = 288.15
    
    pUp: float()
    Tup: float()
    h1: float() = 288.15*1000
    
    pDn: float()
    Tdn: float()
    h2: float() = 288.15*1000
    
    dp: float()
    R: float() = 287.0
    Cp: float() = 1.004*1000
    zeta: float() = 1.0
    Cd: float() =1.0
    AreaMech: float() = 0.001
    rho: float() = 1.0
    m_flow: float() = 0.0
    mh_flow: float() = 0.0
    
    def __init__(self):
        self.pUp= self.p1
        self.Tup= self.T1
        
        self.pDn= self.p2
        self.Tdn= self.T2
        
        self.zeta=1.0
        self.dp= 0.0
        self.AreaMech= 0.001
        
    # ########## end def func ##########
    
    
    def calc_m_flow(self):
        self.zeta= 1.0/(self.Cd**2.0)
        
        if(self.p2 <= self.p1):
            self.pUp= self.p1
            self.Tup= self.T1
            self.pDn= self.p2
            self.Tdn= self.T2
        else:
            self.pUp= self.p2
            self.Tup= self.T2
            self.pDn= self.p1
            self.Tdn= self.T1
        # ##### end if #####
        
        self.h1= self.T1* self.Cp
        self.h2= self.T2* self.Cp
        
        self.rho= self.pUp/(self.R*self.Tup)
        self.dp= self.p1 - self.p2
        
        if(self.dp==0.0):
            self.m_flow= 0.0
            self.mh_flow= 0.0
        elif(self.p2<self.p1):
            self.m_flow= self.AreaMech* (2.0*self.rho*self.dp/self.zeta)**(1.0/2.0)
            self.mh_flow= self.m_flow* self.h1
        elif(self.p1<self.p2):
            self.m_flow= -1.0*self.AreaMech* (2.0*self.rho*(-1.0)*self.dp/self.zeta)**(1.0/2.0)
            self.mh_flow= self.m_flow* self.h1
        
        # ##### end if #####
        
    # ########## end def func ##########
    
    
# ########## end class ##########