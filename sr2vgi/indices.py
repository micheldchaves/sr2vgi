Conventional Vegetation Indices (VIs)

def EVI(b2,b4,b8):
    # Enhanced Vegetation Index (Huete et al., 2002).
    EVI = 2.5*(b8 − b4)/(b8 + 6*b4 − 7.5*b2 + 1)

def NDVI(b4,b8):
    # Normalized Difference Vegetation Index (Rouse Jr et al., 1974).
    NDVI = (b8 – b4)/(b8 + b4)ar l

def NDWI (Gao)(b8,b11):
    # Normalized Difference Vegetation Index (Gao, 1996).
    NDWI (Gao) = (b8 – b11)/(b8 + b11)

def NDWI (McFeeters)(b3,b8):
    # Normalized Difference Vegetation Index (McFeeters, 1996).
    NDWI (McFeeters) = (b3 – b8)/(b3 + b8)

def SAVI(b4,b8):
    # Soil-Adjusted Vegetation Index (Huete, 1988).
    SAVI = ((b8 – b4))/((b8 + b4 + 0.5))*1.5

Derived VIs		

def EVI-2(b4,b8):
    # Enhanced Vegetation Index-2 (Jiang et al., 2008).
    EVI-2 = 2.5*(b8 − b4)/(b8 + 6*b4 + 2.4*b2 + 1)

def GNDVI(b4,b8):
    # Green Normalized Difference Vegetation Index (Gitelson, Kaufman, and Merzlyak, 1996).
    GNDVI = (b8 – b3)/(b8 + b3)

def MSAVI(b4,b8):
    # Modified Soil-Adjusted Vegetation Index (Qi et al., 1994).
    MSAVI = 2*b8 + 1 - √(2*b8 + 1)² - 8*(b8 – b5)/2

def OSAVI(b4,b8):
    # Optimized Soil-Adjusted Vegetation Index (Rondeaux, Steven, and Baret, 1996).
    OSAVI = 1.16*b8 – b4/b8 + b4 + 0.16



Less frequent VIs

def AFRI1.6(b8a,b11):
    # Aerosol Free Vegetation Index 1.6 (Karnieli, Kaufman, Remer, and Wald, 2001).
    AFRI1.6 = b8a - 0.66 * b11/b8a + 0.66 * b11

def ARI(b3,b5):
    # Anthocyanin Reflectance Index (Gitelson, Chivkunova and Merzlyak, 2009).
    ARI	= (1/b3) - (1/b5)

def AVI(b4,b8a):
    # Ashburn Vegetation Index (Ashburn, 1978).
    AVI = 2*b8a - b4

def BAI or BAIS2(b4,b6,b7,b8a,b12):
    # Burned Area Index for Sentinel-2 (Filipponi, 2018).
    BAI or BAIS2 = (1 -√b6*b7*b8a/b4)*(b12 - b8a/√b12 + b8a + 1)

def CIGREEN(b3,b8):
    # Chlorophyll Index Green (Gitelson et al., 2003a).
    CIGREEN	= b8/b3 - 1

def CIRE(b5,b7):
    # Chlorophyll Index Red-edge (Gitelson et al., 2003a).
    CIRE = ((b7/b5) - 1)

def CIRED&RE(b4,b5,b8):
    # Red and red-edge modified Chlorophyll Index ((Xie et al. 2018).
    CIRED&RE = (b8/a*b4 + (1 - a)*b5) – 1
a: between 0 and 1


def CRI700(b2,b5):
    # Carotenoid Reflectance Index 700 (Gitelson, Merzlyak, and Chivkunova, 2001a).
    CRI700 = 1/b2 – 1/b5

def CVI(b2,b4,b8):
    # Chlorophyll Vegetation Index (Hunt et al., 2011).
    CVI = b8*b4/(b3)²

def Datt1(b4,b5,b8):
    # Vegetation Index proposed by Datt (Datt, 1999a).
    Datt1 = (b8 - b5)/(b8 - b4)

def Datt3(b3,b5,b8a):
    # Vegetation Index proposed by Datt (Datt, 1998).
    Datt3 = b8a/b3*b5

def DNVI(b1,b2):
    # Discriminant Normalized Vegetation Index (Manna and Raychawdhuri, 2018).
    DNVI = (b1 - b2)²/ √b1 + b2

def GARI(b2,b3,b4,b8):
    # Green atmospherically resistant vegetation index (Gitelson, Kaufman and Merzlyak, 1996).
    GARI = b8 - [b3 - (b2 - b4)]/b8 + [b3 - (b2 - b4)]

def GCVI(b3,b8):
    # Green Chlorophyll Vegetation Index (Gitelson et al., 2003b).
    GCVI = (b8/b3) – 1

def GRVI(b3,b4):
    # Green-Red Vegetation Index (Tucker, 1979).
    GRVI = (b3 - b4)/(b3 + b4)

def IRECI(b4,b5,b6,b7):
    # Inverted Red-edge (Frampton et al., 2013).
    IRECI = (b7 – b4)/(b5/b6)

def LAnthoC(b3,b5,b7):
    # Leaf Anthocyanid Content (Wulf and Stuhler, 2015).
    LAnthoC = b7/b3 - b5

def LCaroC(b2,b5,b7):
    # Leaf Carotenoid Content (Wulf and Stuhler, 2015).
    LCaroC = b7/b2 - b5

def LChloC(b5,b7):
    # Leaf Chlorophyll Content (Wulf and Stuhler, 2015).
    LChloC = b7/b5

def LSWI(b8,b11):
    # Land Surface Water Index (Xiao et al., 2002).
    LSWI = (b8 – b11)/(b8 + b11)

def Maccioni(b4,b5,b7):
    # Vegetation Index proposed by Maccioni (Maccioni, Agati, and Mazzinghi, 2001).
    Maccioni = (b7 - b5)/(b7 - b4)

def MCARI(b3,b4,b5):
    # Modified Chlorophyll Absorption in Reflectance Index (Daughtry et al. 2000).
    MCARI = ((b5 – b4) − 0.2*(b5 – b3))*(b5/b4)

def MIRBI(b6,b7,b11,b12):
    # Mid Infrared Burned Index (Trigg and Flasse, 2001).
    MIRBI = 10*b7 - 9.8*b6 + 2	10*b12 - 9.8*b11 + 2

def MNDBI(b8,b12):
    # Modified Normalized Difference Built-up Index (Shingare, Hemane, and Dandekar, 2014).
    MNDBI = (b12 - b8)/(b12 + b8)

def MNDVI(b2,b4,b8):
    # Modified Normalized Difference Vegetation Index (Main et al., 2011).
    MNDVI = b8 - b4/b8 + b4 - 2*b2

def MNDWI(b3,b11):
    # Modified Normalized Difference Water Index (Xu, 2006). 
    MNDWI = (b3 - b11)/(b3 + b11)

def MNSI(b3,b4,b6,b8):
    # Misra Non-such Index (Misra, Wheeler, and Oliver, 1977).
    MNSI = 0.404*b3 + 0.039*b4 - 0.505*b6 + 0.762*b8

def MSI(b8a,b11):
    # Moisture Stress Index (Rock, Williams, and Vogelmann, 1985).
    MSI = b11/b8a

def MSR(b4,b5,b8):
    # Modified Simple Ratio (Chen, 1996).
    MSR = b8/b4 - 1/√b8/b5 + 1

def MSRRED&RE(b4,b5,b8):
    # Red and red-edge MSR index (Xie et al. 2018).
    MSRRED&RE = b8/(a*b4 +(1 - a)*b5)-1/√b8(a*b4 +(1 - a)*b5) + 1
where a = between 0 and 1

def MSRRE(b5,b8):
    # Modified Simple Ratio Red-edge (Wu et al., 2008).
    MSRRE = ((b8/b5) − 1)/(√((b8/b5) + 1))

def MSRREn(b5,b8a):
    # Modified Simple Ratio red-edge normalized (Wu et al., 2008).
    MSRREn = ((b8a/b5) −1)/(√((b8a/b5) +1))

def MTCI(b4,b5,b6):
    # MERIS Terrestrial Chlorophyll Index (Dash and Curran, 2004).
    MTCI = (b6 - b5)/(b5 + b4)  

def NBR(b8,b12):
    # Normalized Burn Ratio (García and Caselles, 1991. Named by Key and Benson, 1999).
    NBR = (b8 – b12)/(b8 + b12)

def NBR-2(b11,b12):
    # Normalized Burn Ratio-2 (García and Caselles, 1991).
    NBR-2 = ((b11 – b12))/((b11 + b12))

def NBAaI(b6,b11):
    # Normalized Difference Bareness Index (Zhao and Chen, 2005).
    NDBaI = (b6 - b11)/(b6 + b11)

def NDBI(b8,b11):
    # Normalized Difference Built-up Index (Zha, Gao, and Ni, 2003).
    NDBI = (b11 – b8)/(b11 + b8)

def NDII(b8,b11):
    # Normalized Difference Infrared Index (Hardisky, Klemas and Smart, 1983).
    NDII = (b8 – b11)/(b8 + b11)

def NDMI(b8,b11):
    # Normalized differences moisture index (Gerard et al., 2003).
    NDMI = (b8 - b11)/(b8 + b11)

def NDRE1(b5,b6):
    # Normalized Difference Red-edge (Gitelson and Merzlyak, 1994).
    NDRE1 = (b6 – b5)/(b6 + b5)

def NDRE2(b5,b7):
    # Normalized Difference Red-edge (Barnes et al., 2000).
    NDRE2 = (b7 – b5)/(b7 + b5)

def NDREDGESWIR(b6,b12):
    # Normalized Difference Red-edge and SWIR2 (Radoux et al., 2016).
    NDREDGESWIR = (b6 - b12)/(b6 + b12)

def NDRE1M(b1,b5,b6):
    # Normalized Difference Red-edge 1 modified (Sims and Gamon, 2002).
    NDRE1M = (b6 – b5)/(b6 + b5 - 2* b1)

def NDRE2M(b1,b5,b7):
    # Normalized Difference Red-edge 2 modified (Sims and Gamon, 2002).
    NDRE2M = (b7 – b5)/(b7 + b5 - 2* b1)

def NDSWIR(b8,b12):
    # Normalized Difference SWIR (Gerard et al., 2003).
    NDSWIR = (b8 – b12)/(b8 + b12)

def NDTI(b11,b12):
    # Normalized Difference Tillage Index (Van Deventer et al., 1997).
    NDTI = ((b11 – b12))/((b11 + b12))

def NDVIRE(b5,b8):
    # Normalized Difference Vegetation Index Red-edge (Gitelson and Merzlyak, 1994).
    NDVIRE = (b8 – b5)/(b8 + b5)

def NDVIRE1n(b5,b8a):
    # Normalized Difference Vegetation Index red-edge 1 narrow (Fernández-Manso, Fernández-Manso and Quintano, 2016).
    NDVIRE1n = (b8a - b5)/(b8a + b5)

def NDVIRE2(b6,b8):
    # Normalized Difference Vegetation Index red-edge 2 (Fernández-Manso, Fernández-Manso and Quintano, 2016).
    NDVIRE2 = (b8 - b6)/(b8 + b6)

def NDVIRE2n(b6,b8a):
    # Normalized Difference Vegetation Index red-edge 2 narrow (Fernández-Manso, Fernández-Manso and Quintano, 2016).
    NDVIRE2n = (b8a - b6)/(b8a + b6)

def NDVIRE3(b7,b8):
    # Normalized Difference Vegetation Index red-edge 3 (Gitelson and Merzlyak, 1994).
    NDVIRE3 = (b8 - b7)/(b8 + b7)

def NDVIRE3n(b7,b8a):
    # Normalized Difference Vegetation Index red-edge 3 narrow (Fernández-Manso, Fernández-Manso, and Quintano, 2016).
    NDVIRE3n = (b8a - b7)/(b8a + b7)

def NDVI705(b5,b6):
    # Red-edge Normalized Difference Vegetation Index (Gitelson and Merzlyak, 1994).
    NDVI705 = (b6 - b5)/(b6 + b5)

def NGRDI(b3,b5):
    # Normalized Green Red Difference Index (Zarco-Tejada et al., 2001).
    NGRDI = (b3 - b5)/(b3 + b5)

def NHI(b3,b11):
    # Normalized Humidity Index (Lacaux et al., 2007).
    NHI = (b11 – b3)/(b11 + b3)

def NMDI(b8,b11,b12):
    # Normalized Multi-band Drought Index (Wang and Qu, 2007).
    NMDI = b8 - (b11 – b12)/b8 + (b11 – b12)

def PPR(b2,b3):
    # Plant Pigment Ratio (Metternicht, 2003).
    PPR = (b3 - b2)/(b3 + b2)

def PSRI(b3,b4,b6):
    # Plant Senescence Reflectance Index (Merzlyak et al., 1999).
    PSRI = (b4 – b3)/b6

def PVR(b3,b4):
    # Photosyntetic Vigour Ratio (Metternicht, 2003).
    PVR = (b3 - b4)/(b3 + b4)

def RBNDVI(b2,b4,b8):
    # Red-Blue NDVI (Wang et al., 2007).
    RBNDVI = (b8 - (b4 + b2))/(b8 + (b4 + b2))

def RedSWIR1(b4,b11):
    # Red and SWIR bands difference (Jacques et al., 2014).
    RedSWIR1 = b4 - b11

def REIP(b4,b5,b6,b7):
    # Red-edge Inflection Point (Herrmann et al. 2011).
    REIP = 700 + 40*((b4 + b7/2) - b5/b6 - b5)

def RERVI(b5,b8):
    # Red-edge ratio vegetation index (Cao et al., 2013).
    RERVI = b8/b5

def REPA(b4,b5,b6,b7):
    # Red-edge Peak Area (Radoux et al. 2016).
    REPA = b4 + b5 + b6 + b7 + b8a

def RTVIcore(b3,b5,b8):
    # Red-edge Triangular Vegetation Index (Chen et al., 2010).
    RTVIcore = 100*(b8 – b5) - 10*(b8 – b3)

def SAVIR&RE(b4,b5,b8):
    # Soil-Adjusted Vegetation Index with red and red-edge (Vincent, Kumar, and Upadhyay, 2020).
    SAVIR&RE = (1 + L)(b8 - (ab4 +(1 - a)b5))/b5 + L+ (ab4 + (1 - a)*b5)

def SIPI(b3,b4,b8):
    # Structure Intensive Pigment Index (Peñuelas, Baret and Filella, 1995).
    SIPI = b3/b8 - b4

def SIWSI(b8a,b11):
    # Shortwave Infrared Water Stress Index (Fensholt and Sandholt, 2003).
    SIWSI = (b8a - b11)/(b8a + b11)

def SRI(b4,b8):
    # Simple Ratio Index (Jordan, 1969).
    SRI = b8/b4

def SRNIRnarrowGreen(b3,b8a):
    # Simple ratio NIR narrow and Green (le Maire, François, and Dufrêne, 2004).
    SRNIRnarrowGreen = b8a/b3

def SRNIRnarrowRed(b4,b8a):
    # Simple ratio NIR narrow and Red (Blackburn, 1998).
    SRNIRnarrowRed = b8a/b4

def SRNIRnarrowRE1(b5,b8a):
    # Simple NIR and Red-edge 1 Ratio (Datt, 1999b).
    SRNIRnarrowRE1 = b8a/b5

def SRNIRnarrowRE2(b6,b8a):
    # Simple NIR and Red-edge 2 Ratio (Datt, 1999b).
    SRNIRnarrowRE2 = b8a/b6

def SRNIRnarrowRE3(b7,b8a):
    # Simple NIR and Red-edge 3 Ratio (Datt, 1999b).
    SRNIRnarrowRE3 = b8a/b7

def SRRE1(b1,b6):
    # Surface Reflectance Red-edge 1 (Sims and Gamon, 2002).
    SRRE1 = (b6 - b1)/(b6 - b1)

def SRRE2(b1,b5,b7):
    # Surface Reflectance Red-edge 2 (Sims and Gamon, 2002).
    SRRE2 = (b7 - b1)/(b5 - b1)

def STI(b11,b12):
    # Soil Tillage Index (Van Deventer, 1997).
    STI = b11/b12

def S2REP(b4,b5,b6,b7):
    # Sentinel-2 Red-edge position (Frampton et al., 2013).
    S2REP = 700 + 35*((((b7 – b4/2) – b5)/b6-b5))

def TCARI(b3,b4,b5):
    # Transformed Chlorophyll Absorption in Reflectance Index (Daughtry et al., 2000).
    TCARI = 3[(b5 – b4) − 0.2(b5 – b3)(b5/4)]

def TVI(b3,b4,b6):
    # Transformed Vegetation Index (Broge and Leblanc, 2001).
    TVI = 0.5 * (120 * (b6 – b3) – 200 * (b4 – b3))

def VARIGREEN(b2,b3,b4):
    # Visible atmospherically resistant index green (Gitelson et al. 2001a).
    VARIGREEN = (b3 - b4)/(b3 + b4 - b2)

def VI700(b4,b5):
    # Vegetation Index 700 (Gitelson et al., 2002).
    VI700 = (b5 - b4)/(b5 + b4)

def VSDI(b2,b4,b11):
    # Visible and Shortwave Infrared Drought Index (Zhang et al., 2013).
    VSDI = 1 - [(b11 - b2)+(b4 - b2)]

def WBI(b2,b4):
    # Water Body Index (Domenech and Mallet, 2014).
    WBI = b2 - b4/b2 + b4

def WDRVIRE(b5,b7):
    # Wide Dynamic Range Vegetation Index (Peng and Gitelson, 2011).
    WDRVIRE = (0.01*b7 – b5/0.01*b7 + b5) + (1 – 0.01/1 + 0.01)



References

1.	Ashburn, P. 1978. The vegetative index number and crop identification. The LACIE Symposium Proceedings of the Technical Session, 843-855. 

2.	Barnes, E., Clarke, T., Richards, S., Colaizzi, P., Haberland, J., Kostrzewski, M., et al. (2000). Coincident detection of crop water stress, nitrogen status and canopy density using ground based multispectral data. in: P. C. Robert, R. H. Rust, & W. E. Larson (Eds.), Proceedings of the 5th International Conference on Precision Agriculture, 16–19 July 2000. Bloomington, USA.

3.	Blackburn, G.A. 1998. Quantifying chlorophylls and caroteniods at leaf and canopy scales. Remote Sensing of Environment 66, 273–285. doi:10.1016/S0034-4257(98)00059-5.

4.	Broge, N.H., Leblanc, E., 2001. Comparing prediction power and stability ofbroadband and hyperspectral vegetation indices for estimation of green leaf area index and canopy chlorophyll density. Remote Sensing of Environment 76, 156–172. doi:10.1016/S0034-4257(00)00197-8.

5.	Cao, Q.; Miao, Y.; Wang, H.; Huang, S.; Cheng, S.; Khosla, R.; Jiang, R. 2013. Non-destructive estimation of rice plant nitrogen status with Crop Circle multispectral active canopy sensor. Field Crops Research 154, 133–144. doi:10.1016/j.fcr.2013.08.005.

6.	Chen, J. 1996. Evaluation of vegetation indices and modified simple ratio for boreal applications. Canadian Jurnal of Remote Sensing 22, 229–242. doi:10.1080/07038992.1996.10855178.

7.	Chen, P. F., Nicolas, T., Wang, J. H., Philippe, V., Huang, W. J., Li, B. G. 2010. New index for crop canopy fresh biomass estimation. Spectroscopy and Spectral Analysis 30(2), 512-517. 10.3964/j.issn.1000-0593(2010)02-0512-06.

8.	Dash, J., Curran, P.J., 2004. The MERIS terrestrial chlorophyll index. International Journal of Remote Sensing 25, 5403–5413. doi:10.1080/0143116042000274015.

9.	Datt, B. 1998. Remote sensing of chlorophyll a, chlorophyll b, chlorophyll a + b, and total carotenoid content in eucalyptus leaves. Remote Sensing of Environment, 66, 111–121. doi:10.1016/S0034-4257(98)00046-7.

10.	Datt, B. 1999a. Remote sensing of water content in Eucalyptus leaves. Australian Journal of Botany 47, 909–923. doi:10.1071/BT98042.

11.	Datt, B. 1999b. Visible/near infrared reflectance and chlorophyll content in Eucalyptus leaves. International Journal of Remote Sensing 20, 2741–2759. doi:10.1080/014311699211778.

12.	Daughtry, C. S. T., Walthall, C. L., Kim, M. S., De Colstoun, E. B., McMurtrey Iii, J. E. 2000. Estimating corn leaf chlorophyll concentration from leaf and canopy reflectance. Remote Sensing of Environment 74(2), 229-239. doi:10.1016/S0034-4257(00)00113-9.

13.	Diniz, C., Cortinhas, L., Nerino, G., Rodrigues, J., Sadeck, L., Adami, M., Souza-Filho, P. W. M. 2019. Brazilian mangrove status: Three decades of satellite data analysis. Remote Sensing, 11(7), 808. doi: 10.3390/rs11070808.

14.	Domenech, E., Mallet, C. 2014. Change Detection in High resolution land use/land cover geodatabases (at object level). EuroSDR official publication, 64.

15.	Fensholt, R., Sandholt, I. 2003. Derivation of a shortwave infrared water stress index from MODIS near- and shortwave infrared data in a semiarid environment. Remote Sensing of Environment 87, 111–121. doi:10.1016/j.rse.2003.07.002.

16.	Fernández-Manso, A., Fernández-Manso, O., Quintano, C. 2016. SENTINEL-2A red-edge spectral indices suitability for discriminating burn severity. International Journal Of Applied Earth Observation and Geoinformation 50, 170-175. doi:10.1016/j.jag.2016.03.005.

17.	Filipponi, F. 2018. BAIS2: burned area index for Sentinel-2. in: Multidisciplinary Digital Publishing Institute Proceedings (Vol. 2, No. 7, p. 364). doi:10.3390/ecrs-2-05177.

18.	Frampton, W.J., Dash, J., Watmough, G., Milton, E.J. 2013. Evaluating the capabilities of Sentinel-2 for quantitative estimation of biophysical variables in vegetation. ISPRS Journal of Photogrammetry and Remote Sensing 82, 83–92. doi:10.1016/j.isprsjprs.2013.04.007.

19.	Gao, B. 1996. NDWI - A normalized difference water index for remote sensing of vegetation liquid water from space. Remote Sensing of Environment 58(3), 257–266. doi:10.1016/s0034-4257(96)00067-3.

20.	García, M. J. L., Caselles, V. 1991. Mapping burns and natural reforestation using thematic Mapper data. Geocarto International 6(1), 31–37. doi:10.1080/10106049109354290.

21.	Gerard, F., Plummer, S., Wadsworth, R., Sanfeliu, A. F., Iliffe, L., Balzter, H., & Wyatt, B. 2003. Forest fire scar detection in the boreal forest with multitemporal SPOT-VEGETATION data. IEEE Transactions on Geoscience and Remote Sensing 41(11), 2575–2585. doi:10.1109/tgrs.2003.819190.

22.	Gitelson, A., Merzlyak, M. N. 1994. Spectral reflectance changes associated with autumn senescence of Aesculus hippocastanum L. and Acer platanoides L. leaves. Spectral features and relation to chlorophyll estimation. Journal of Plant Physiology 143(3), 286-292. doi:10.1016/S0176-1617(11)81633-0.

23.	Gitelson, A., Kaufman, Y. J., Merzlyak, M. N. 1996. Use of a green channel in remote sensing of global vegetation from EOS-MODIS. Remote Sensing of Environment 58(3), 289–298. doi:10.1016/s0034-4257(96)00072-7.

24.	Gitelson, A., Merzlyak, M. N., Chivkunova, O. B. 2001a. Optical properties and nondestructive estimation of anthocyanin content in plant leaves. Photochemistry and Photobiology, 74,38–45. doi:10.1562/0031-8655(2001)074<0038:opaneo>2.0.co;2.

25.	Gitelson, A., Merzlyak, M. N., Zur, Y., Stark, R., Gritz, U. 2001. Non-destructive and remote sensing techniques for estimation of vegetation status. in: Third European Conference on Precision Agriculture (Montpellier, France, 2001), pp. 301-306.

26.	Gitelson, A. A., Kaufman, Y. J., Stark, R., Rundquist, D. 2002. Novel algorithms for remote estimation of vegetation fraction. Remote sensing of Environment 80(1), 76-87. doi:10.1016/S0034-4257(01)00289-9.

27.	Gitelson, A. A., Gritz, Y., Merzlyak, M. N. 2003a. Relationships between leaf chlorophyll content and spectral reflectance and algorithms for non-destructive chlorophyll assessment in higher plant leaves. Journal of Plant Physiology 160(3), 271–282. doi:10.1078/0176-1617-00887.

28.	Gitelson, A. A., Viña, A., Arkebauer, T. J., Rundquist, D. C., Keydan, G., Leavitt, B. 2003b. Remote estimation of leaf area index and green leaf biomass in maize canopies. Geophysical Research Letters 30(5). doi:10.1029/2002gl016450.

29.	Gitelson, A. A., Chivkunova, O. B., Merzlyak, M. N. 2009. Nondestructive estimation of anthocyanins and chlorophylls in anthocyanic leaves. American Journal of Botany 96(10), 1861-1868. doi:10.3732/ajb.0800395.

30.	Gupta, K., Mukhopadhyay, A., Giri, S., Chanda, A., Majumdar, S. D., Samanta, S., ... Hazra, S. 2018. An index for discrimination of mangroves from non-mangroves using LANDSAT 8 OLI imagery. MethodsX 5, 1129-1139. doi:10.1016/j.mex.2018.09.011.

31.	Hardisky, M.A., Klemas, V. and Smart, R.M. 1983. The Influence of Soil Salinity, Growth Form, and Leaf Moisture on the Spectral Radiance of Spartina alterniflora Canopies. Photogrammetric Engineering and Remote Sensing 49, 77-83.

32.	Klemas, V., Smart, R. M. 1983. The Influence of Soil Salinity, Growth Form, and Leaf Moisture on-the Spectral Radiance of. Photogrammetric Engineering and Remote Sensing 49(1), 77-83.

33.	Herrmann, I., Pimstein, A., Karnieli, A., Cohen, Y., Alchanatis, V., Bonfil, D. J. 2011. LAI assessment of wheat and potato crops by VENμS and Sentinel-2 bands. Remote Sensing of Environment 115, 2141–2151. doi:10.1016/j.rse.2011.04.018.

34.	Huete, A. 1988. A soil-adjusted vegetation index (SAVI). Remote Sensing of Environment 25(3), 295–309. doi:10.1016/0034-4257(88)90106-x.

35.	Huete, A., Didan, K., Miura, T., Rodriguez, E. P., Gao, X., Ferreira, L. G. 2002. Overview of the radiometric and biophysical performance of the MODIS vegetation indices. Remote Sensing of Environment 83(1-2), 195-213. doi:10.1016/S0034-4257(02)00096-2.

36.	Hunt, E. R., Daughtry, C. S. T., Eitel, J. U. H., Long, D. S. 2011. Remote sensing leaf chlorophyll content using a visible Band index. Agronomy Journal 103, 1090–1099. doi:10.2134/agronj2010.0395.

37.	Jacques D.C. et al., 2014. Monitoring dry vegetation masses in semi-arid areas with MODIS SWIR bands. Remote Sensing of Environment 153, 40-49. doi:10.1016/j.rse.2014.07.027.

38.	Jiang, Z., Huete, A. R., Didan, K., Miura, T. 2008. Development of a two-band enhanced vegetation index without a blue band. Remote sensing of Environment 112(10), 3833-3845. doi:10.1016/j.rse.2008.06.006.

39.	Jordan, C.F. 1969. Derivation of leaf-area index from quality of light on the forest floor. Ecology 50, 663–666. doi:10.2307/1936256.

40.	Karnieli, A., Kaufman, Y. J., Remer, L., Wald, A. 2001. AFRI – aerosol free vegetation index. Remote Sensing of Environment 77,10–21. doi:10.1016/S0034-4257(01)00190-0.

41.	Key, C.H., Benson, N., 1999. The Normalized Burn Ratio (NBR): A Landsat TM Radiometric Measure of Burn Severity. United States Geological Survey, Northern Rocky Mountain Science Center. (Bozeman, MT).

42.	Lacaux, J.P.; Tourre, Y.M.; Vignolles, C.; Ndione, J.A.; Lafaye, M. 2007. Classification of ponds from high-spatial resolution remote sensing: Application to Rift Valley Fever epidemics in Senegal. Remote Sensing of Environment 106, 66–74. doi:10.1016/j.rse.2006.07.012.

43.	le Maire, G.; François, C.; Dufrêne, E. 2004. Towards universal broad leaf chlorophyll indices using PROSPECT simulated database and hyperspectral reflectance measurements. Remote Sensing of Environment 89, 1–28. doi:10.1016/j.rse.2003.09.004.

44.	Metternicht, G. 2003. Vegetation indices derived from high-resolution airborne videography for precision crop management. International Journal of Remote Sensing 24(14), 2855-2877. doi:10.1080/01431160210163074.

45.	Maccioni, A., Agati, G., Mazzinghi, P. 2001. New vegetation indices for remote measurement of chlorophylls based on leaf directional reflectance spectra. Journal of Photochemistry and Photobiology B: Biology 61(1-2), 52-61. doi:10.1016/S1011-1344(01)00145-2.

46.	Main, R., Cho, M. A., Mathieu, R., O’kennedy, M. M., Ramoelo, A., Koch, S. 2011. An investigation into robust spectral indices for leaf chlorophyll estimation. ISPRS Journal of Photogrammetry and Remote Sensing 66, 751–761. doi:10.1016/j.isprsjprs.2011.08.001.

47.	Manna, S., Raychaudhuri, B. 2018. Mapping distribution of Sundarban mangroves using Sentinel-2 data and new spectral metric for detecting their health condition. Geocarto International 35(4), 434-452. doi:10.1080/10106049.2018.1520923.

48.	McFeeters, S. K. 1996. The use of the Normalized Difference Water Index (NDWI) in the delineation of open water features. International Journal of Remote Sensing 17(7), 1425-1432. doi:10.1080/01431169608948714.

49.	Merzlyak, M.N.; Gitelson, A.A.; Chivkunova, O.B.; Rakitin, V.Y. 1999. Non-destructive optical detection of pigment changes during leaf senescence and fruit ripening. Physiologia Plantarum 106, 135–141. doi:10.1034/j.1399-3054.1999.106119.x.

50.	Misra, P. N., Wheeler, S. G., Oliver, R. E. 1977. Kauth-Thomas brightness and greenness axes. in: Contract NASA 9-14350, 23–46.

51.	Müller, H., Rufin, P., Griffiths, P., Siqueira, A. J. B., Hostert, P. 2015. Mining dense Landsat time series for separating cropland and pasture in a heterogeneous Brazilian savanna landscape. Remote Sensing of Environment 156, 490-499. doi:10.1016/j.rse.2014.10.014.

52.	Peng, Y., Gitelson, A. A. 2011. Application of chlorophyll-related vegetation indices for remote estimation of maize productivity. Agricultural and Forest Meteorology 151(9), 1267-1276. doi:10.1016/j.agrformet.2011.05.005.

53.	Peñuelas, J., Baret, F., Filella, I. 1995. Semi-empirical indices to assess carotenoids/chlorophyll-a ratio from leaf spectral reflectance. Photosynthetica 31, 221–230.

54.	Pinty, B., Verstraete, M. M. 1992. GEMI: A non-linear index to monitor global vegetation from satellites. Vegetatio 101,15–20. doi:10.1007/BF00031911.

55.	Piyoosh, A.K.; Ghosh, S.K. 2018. Development of a modified bare soil and urban index for Landsat 8 satellite data. Geocarto International 33, 423–442. doi:10.1080/10106049.2016.1273401.

56.	Qi, J., Chehbouni, A., Huete, A. R., Kerr, Y. H., Sorooshian, S. 1994. A modified soil adjusted vegetation index. Remote Sensing of Environment 48(2), 119-126. doi:10.1016/0034-4257(94)90134-1.

57.	Radoux, J., Chomé, G., Jacques, D. C., Waldner, F., Bellemans, N., Matton, N., ... Defourny, P. 2016. Sentinel-2’s potential for sub-pixel landscape feature detection. Remote Sensing 8(6), 488. doi:10.3390/rs8060488.

58.	Rasul, A., Balzter, H., Ibrahim, G. R. F., Hameed, H. M., Wheeler, J., Adamu, B., ... Najmaddin, P. M. 2018. Applying Built-Up and Bare-Soil Indices from Landsat 8 to Cities in Dry Climates. Land 7(3), 81. doi:10.3390/land7030081.

59.	Rock, B.N., Williams, D.L., Vogelmann, J.E. 1985. Field and airborne spectral characterization of suspected acid deposition damage in red spruce (picea rubens) from vermont. in: Proceedings of the 11th International Symposium—Machine Processing of Remotely Sensed Data, West Lafayette, IN, USA, 25–27 June 1985; pp. 71–81.

60.	Rondeaux, G., Steven, M., Baret, F. 1996. Optimization of soil-adjusted vegetation indices. Remote Sensing of Environment 55, 95–107. doi:10.1016/0034-4257(95)00186-7.

61.	Rouse, J. W., Haas, R. H., Schell, J. A., Deering, D. W. 1974. Monitoring vegetation systems in the great plains with ERTS. in: Proceedings of the Third Earth Resources Technology Satellite-1 Symposium; NASA SP-351 (pp. 309-317).

62.	Sims, D.A., Gamon, J.A., 2002. Relationships between leaf pigment content and spectral reflectance across a wide range of species, leaf structures and developmental stages. Remote Sensing of Environment 81, 337–354. doi:10.1016/S0034-4257(02)00010-X.

63.	Shingare, P.P., Hemane, P.M., Dandekar, D.S., 2014. Fusion classification of multispectral and panchromatic image using improved decision tree algorithm. in: International Conference on Signal Propagation and Computer Technology (ICSPCT) 2014, pp. 598–603. doi:10.1109/ICSPCT.2014.6884944.

64.	Souza Jr, C.M., Roberts, D.A., Cochrane, M.A. 2005. Combining spectral and spatial information to map canopy damage from selective logging and forest fires. Remote Sensing of Environment 98, 329–343. doi:10.1016/j.rse.2005.07.013.

65.	Trigg, S., Flasse, S. 2001. An evaluation of different bi-spectral spaces for discriminating burned shrub-savannah. International Journal of Remote Sensing 22(13), 2641–2647. doi:10.1080/01431160110053185.

66.	Tucker, C.J. 1979. Red and photographic infrared linear combinations for monitoring vegetation. Remote Sensing of Environment 8, 127–150. doi:10.1016/0034-4257(79)90013-0.

67.	Van Deventer, A. P., Ward, A. D., Gowda, P. H., Lyon, J. G. 1997. Using thematic mapper data to identify contrasting soil plains and tillage practices. Photogrammetric Engineering and Remote Sensing 63, 87-93.

68.	Vincent, A., Kumar, A., Upadhyay, P. 2020. Effect of Red-Edge Region in Fuzzy Classification: A Case Study of Sunflower Crop. Journal of the Indian Society of Remote Sensing 1-13. doi:10.1007/s12524-020-01109-4.

69.	Xiao, X., Boles, S., Liu, J., Zhuang, D., Liu, M. 2002. Characterization of forest types in Northeastern China, using multi-temporal SPOT-4 VEGETATION sensor data. Remote Sensing of Environment 82(2-3), 335-348. doi:10.1016/s0034-4257(02)00051-2.

70.	Xie, Q., Dash, J., Huang, W., Peng, D., Qin, Q., Mortimer, H., ... Dong, Y. 2018. Vegetation indices combining the red and red-edge spectral information for leaf area index retrieval. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 11(5), 1482-1493. doi:10.1109/JSTARS.2018.2813281.

71.	Xu, H. (2006). Modification of normalised difference water index (NDWI) to enhance open water features in remotely sensed imagery. International Journal of Remote Sensing 27(14), 3025–3033. doi:10.1080/01431160600589179.

72.	Xu, H. 2008. A new index for delineating built-up land features in satellite imagery. International Journal of Remote Sensing 29(14), 4269-4276. doi:10.1080/01431160802039957.

73.	Zarco-Tejada, P. J., Miller, J. R., Noland, T. L., Mohammed, G. H., Sampson, P. H. 2001. Scaling-up and model inversion methods with narrowband optical indices for chlorophyll content estimation in closed forest canopies with hyperspectral data. IEEE Transactions on Geoscience and Remote Sensing 39, 1491–1507. doi:10.1109/36.934080.

74.	Zha, Y.; Gao, J.; Ni, S. 2003. Use of normalized difference built-up index in automatically mapping urban areas from TM imagery. International Journal of Remote Sensing 24, 583–594. doi:10.1080/01431160304987.

75.	Zhang, N., Hong, Y., Qin, Q., Liu, L. 2013. VSDI: a visible and shortwave infrared drought index for monitoring soil and vegetation moisture based on optical remote sensing. International Journal of Remote Sensing 34(13), 4585-4609. doi:10.1080/01431161.2013.779046.

76.	Zhao, H., Chen, X., 2005. Use of normalized difference bareness index in quickly mapping bare areas from TM/ETM+. in: Proceedings of the 2005 IEEE International Geoscience and Remote Sensing Symposium 3, pp. 1666. doi:10.1109/IGARSS.2005.1526319.

77.	Wang, L., Qu, J. J. 2007. NMDI: A normalized multi‐band drought index for monitoring soil and vegetation moisture with satellite remote sensing. Geophysical Research Letters 34(20). doi:10.1029/2007GL031021.

78.	Wang, F. M., Huang, J. F., Tang, Y. L., Wang, X. Z. 2007. New vegetation index and its application in estimating leaf area index of rice. Rice Science 14(3), 195-203. doi:10.1016/S1672-6308(07)60027-4.

79.	Wu, C., Niu, Z., Tang, Q., Huang, W. 2008. Estimating chlorophyll content from hyperspectral vegetation indices: Modeling and validation. Agricultural and Forest Meteorology 148(8-9), 1230-1241. doi:10.1016/j.agrformet.2008.03.005.

80.	Wulf, H.; Stuhler, S. 2015. Sentinel-2: Land Cover, Preliminary User Feedback on Sentinel-2A Data. in: Proceedings of the Sentinel-2A Expert Users Technical Meeting, Frascati, Italy, 29–30 September 2015.
