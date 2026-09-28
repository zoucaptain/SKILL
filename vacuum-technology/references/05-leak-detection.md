# Leak Detection (Leybold)

## Page 7

6
Table of Contents
4.
Analysis of gas at low pressures using 
mass spectrometry  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .95
4.1
General  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .95
4.2
A historical review  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .95
4.3
The quadrupole mass spectrometer (TRANSPECTOR)  . . . . . .96
4.3.1
Design of the sensor  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .96
4.3.1.1
The normal (open) ion source  . . . . . . . . . . . . . . . . . . . . . . . . . .96
4.3.1.2
The quadrupole separation system  . . . . . . . . . . . . . . . . . . . . . .97
4.3.1.3
The measurement system (detector) . . . . . . . . . . . . . . . . . . . . .98
4.4
Gas admission and pressure adaptation  . . . . . . . . . . . . . . . . . .99
4.4.1
Metering valve  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .99
4.4.2
Pressure converter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .99
4.4.3
Closed ion source (CIS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .99
4.4.4
Aggressive gas monitor (AGM)  . . . . . . . . . . . . . . . . . . . . . . . . .99
4.5
Descriptive values in mass spectrometry (specifications)  . . . .101
4.5.1
Line width (resolution)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .101
4.5.2
Mass range  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .101
4.5.3
Sensitivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .101
4.5.4
Smallest detectable partial pressure  . . . . . . . . . . . . . . . . . . . .101
4.5.5
Smallest detectable partial pressure ratio (concentration) . . . .101
4.5.6
Linearity range  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .102
4.5.7
Information on surfaces and amenability to bake-out  . . . . . . .102
4.6
Evaluating spectra  . . . . . . . . . . . . . . . 

## Page 11

10
Vacuum physics
Avogadro’s number (or constant) NA indicates how many gas particles will
be contained in a mole of gas. In addition to this, it is the proportionality
factor between the gas constant R and Boltzmann’s constant k:
R = NA · k
(1.4)
Derivable directly from the above equations (1.1) to (1.4) is the correlation
between the pressure p and the gas density ρ of an ideal gas.
R · T
p = ρ ⋅
(1.5)
M
In practice we will often consider a certain enclosed volume V in which the
gas is present at a certain pressure p. If m is the mass of the gas present
within that volume, then 
m
ρ = −−− 
(1.6)
V
The ideal gas law then follows directly from equation (1.5):
m
p ⋅ V = −−− ⋅ R ⋅ T = ν ⋅ R ⋅ T
(1.7)
M
Here the quotient m / M is the number of moles υ present in volume V.
The simpler form applies for m / M = 1, i.e. for 1 mole:
p · V = R · T
(1.7a)
The following numerical example is intended to illustrate the correlation
between the mass of the gas and pressure for gases with differing molar
masses, drawing here on the numerical values in Table IV (Chapter 9).
Contained in a 10-liter volume, at 20 °C, will be 
a)  1g of helium
b)  1g of nitrogen
When using the equation (1.7) there results then at V = 10 l  , m = 1 g, 
R = 83.14 mbar · l · mol–1 · K–1, T = 293 K (20 °C) 
In case a) where M = 4 g · mole-1 (monatomic gas):
In case b), with M = 28 ≠g mole-1 (diatomic gas):
The result, though appearing to be paradoxical, is that a certain mass of a
light gas exerts a greater pressure than the same mass of a heavier gas. If
one takes into account, however, that at the same gas density (see
Equation 1.2) more particles of a lighter gas (large n, small m) will be pre-
sent than for the heavier gas (small n, large m), the results become more
understandable since only the particle number density n is determinant for
the pressure level, assuming equal temperature (see Equation 1.1).
The main task of vacuum technology is to reduce the particle number den-
sity n inside a given vol

## Page 13

12
Vacuum physics
Leak rate qL (mbar · l · s–1)
According to the definition formulated above it is easy to understand that
the size of a gas leak, i.e. movement through undesired passages or “pipe”
elements, will also be given in mbar · l · s–1. A leak rate is often measured
or indicated with atmospheric pressure prevailing on the one side of the
barrier and a vacuum at the other side (p < 1 mbar). If helium (which may
be used as a tracer gas, for example) is passed through the leak under
exactly these conditions, then one refers to “standard helium conditions”.
Outgassing (mbar · l)
The term outgassing refers to the liberation of gases and vapors from the
walls of a vacuum chamber or other components on the inside of a vacuum
system. This quantity of gas is also characterized by the product of p · V,
where V is the volume of the vessel into which the gases are liberated, and
by p, or better Δp, the increase in pressure resulting from the introduction
of gases into this volume.
Outgassing rate (mbar · l · s–1)
This is the outgassing through a period of time, expressed in mbar · l · s–1. 
Outgassing rate (mbar · l · s–1 · cm–2)
(referenced to surface area)
In order to estimate the amount of gas which will have to be extracted,
knowledge of the size of the interior surface area, its material and the sur-
face characteristics, their outgassing rate referenced to the surface area
and their progress through time are important.
Mean free path of the molecules λ (cm) and collision rate z (s-1)
The concept that a gas comprises a large number of distinct particles
between which – aside from the collisions – there are no effective forces,
has led to a number of theoretical considerations which we summarize
today under the designation “kinetic theory of gases”.
One of the first and at the same time most beneficial results of this theory
was the calculation of gas pressure p as a function of gas density and the
mean square of velocity c2 for the individual gas molecules in the 

## Page 19

Vacuum physics
18
When working with other gases it will be necessary to multiply the conduc-
tance values specified for air by the factors shown in Table 1.1.
Nomographic determination of conductance values
The conductance values for piping and openings through which air and
other gases pass can be determined with nomographic methods. It is pos-
sible not only to determine the conductance value for piping at specified
values for diameter, length and pressure, but also the size of the pipe diam-
eter required when a pumping set is to achieve a certain effective pumping
speed at a given pressure and given length of the line. It is also possible to
establish the maximum permissible pipe length where the other parameters
are known. The values obtained naturally do not apply to turbulent flows. In
doubtful situations, the Reynolds number Re (see Section 1.5.) should be
estimated using the relationship which is approximated below
(1.31)
Here qpV = S · p is the flow output in mbar l/s, d the diameter of the pipe
in cm. 
A compilation of nomograms which have proved to be useful in practice will
be found in Chapter 9.
1.5.4
Conductance values for other elements
Where the line contains elbows or other curves (such as in right-angle
valves), these can be taken into account by assuming a greater effective
length leff of the line. This can be estimated as follows:
(1.32)
Where
laxial
: axial length of the line (in cm)
leff
: Effective length of the line (in cm)
d
: Inside diameter of the line (in cm)
θ
: Angle of the elbow (degrees of angle)
l
l
d
eff
axial
=
+
·
°·
133 180
.
θ
Re =
·
15 q
d
pV
The technical data in the Leybold catalog states the conductance values for
vapor barriers, cold traps, adsorption traps and valves for the molecular
flow range. At higher pressures, e.g. in the Knudsen and laminar flow
ranges, valves will have about the same conductance values as pipes of
corresponding nominal diameters and axial lengths. In regard to right-angle
valves the conductance c

## Page 21

Vacuum generation
20
2.1.1
Oscillation displacement vacuum pumps
2.1.1.1 Diaphragm pumps
Recently, diaphragm pumps have becoming ever more important, mainly
for environmental reasons. They are alternatives to water jet vacuum
pumps, since diaphragm pumps do not produce any waste water. Overall, a
diaphragm vacuum pump can save up to 90 % of the operating costs
compared to a water jet pump. Compared to rotary vane pumps, the
pumping chamber of diaphragm pumps are entirely free of oil. By design,
no oil immersed shaft seals are required. Diaphragm vacuum pumps are
single or multi-stage dry compressing vacuum pumps (diaphragm pumps
having up to four stages are being manufactured). Here the circumference
of a diaphragm is tensioned between a pump head and the casing wall
(Fig. 2.1). It is moved in an oscillating way by means of a connecting rod
and an eccentric. The pumping or compression chamber, the volume of
which increases and decreases periodically, effects the pumping action.
The valves are arranged in such a way that during the phase where the
volume of the pumping chamber increases it is open to the intake line.
During compression, the pumping chamber is linked to the exhaust line.
The diaphragm provides a hermetic seal between the gear chamber and
the pumping chamber so that it remains free of oil and lubricants (dry
compressing vacuum pump). Diaphragm and valves are the only
components in contact with the medium which is to be pumped. When
coating the diaphragm with PTFE (Teflon) and when manufacturing the inlet
and exhaust valves of a highly fluorinated elastomer as in the case of the
DIVAC from LEYBOLD, it is then possible to pump aggressive vapors and
gases. It is thus well suited for vacuum applications in the chemistry lab.
Due to the limited elastic deformability of the diaphragm only a
comparatively low pumping speed is obtained. In the case of this pumping
principle a volume remains at the upper dead center – the so called “dead
space” – from where the

## Page 51

50
Barrier gas operation
In the case of pumps equipped with a barrier gas facility, inert gas – such
as dry nitrogen – may be applied through a special flange so as to protect
the motor space and the bearings against aggressive media. A special
barrier gas and venting valve meters the necessary quantity of barrier gas
and may also serve as a venting valve.
Decoupling of vibrations
TURBOVAC pumps are precisely balanced and may generally be
connected directly to the apparatus. Only in the case of highly sensitive
instruments, such as electron microscopes, is it recommended to install
vibration absorbers which reduce the present vibrations to a minimum. For
magnetically suspended pumps a direct connection to the vacuum
apparatus will usually do because of the extremely low vibrations produced
by such pumps.
For special applications such as operation in strong magnetic fields,
radiation hazard areas or in a tritium atmosphere, please contact our
Technical Sales Department which has the necessary experience and
which is available to you at any time.
2.1.8
Sorption pumps
The term “sorption pumps” includes all arrangements for the removal of
gases and vapors from a space by sorption means. The pumped gas
particles are thereby bound at the surfaces or in the interior of these
agents, by either physical temperature-dependent adsorption forces (van
der Waals forces), chemisorption, absorption, or by becoming embedded
during the course of the continuous formation of new sorbing surfaces. By
comparing their operating principles, we can distinguish between
adsorption pumps, in which the sorption of gases takes place simply by
temperature-controlled adsorption processes, and getter pumps, in which
the sorption and retention of gases are essentially caused by the formation
of chemical compounds. Gettering is the bonding of gases to pure, mostly
metallic surfaces, which are not covered by oxide or carbide layers. Such
surfaces always form during manufacture, installation or while v

## Page 53

Vacuum generation
52
shortest path and bombard the cathode.
The discharge current i is proportional to the number density of neutral
particles n0, the electron density n-, and the length l of the total discharge
path:
i = n0 · n– · σ · l
(2.25)
The effective cross section s for ionizing collisions depends on the type of
gas. According to (2.25), the discharge current i is a function of the number
particle density n0, as in a Penning gauge, and it can be used as a
measure of the pressure in the range from 10-4 to 10-8 mbar. At lower
pressures the measurements are not reproducible due to interferences
from field emission effects.
In diode-type, sputter-ion pumps, with an electrode system configuration
as shown in Fig. 2.62, the getter films are formed on the anode surfaces
and between the sputtering regions of the opposite cathode. The ions are
buried in the cathode surfaces. As cathode sputtering proceeds, the buried
gas particles are set free again. Therefore, the pumping action for noble
gases that can be pumped only by ion burial will vanish after some time
and a “memory effect” will occur. 
Unlike diode-type pumps, triode sputter-ion pumps exhibit excellent
stability in their pumping speed for noble gases because sputtering and film
forming surfaces are separated. Fig. 2.63 shows the electrode configuration
of triode sputter-ion pumps. Their greater efficiency for pumping noble
gases is explained as follows: the geometry of the system favors grazing
incidence of the ions on the titanium bars of the cathode grid, whereby the
sputtering rate is considerably higher than with perpendicular incidence.
The sputtered titanium moves in about the same direction as the incident
ions. The getter films form preferentially on the third electrode, the target
plate, which is the actual wall of the pump housing. There is an increasing
yield of ionized particles that are grazingly incident on the cathode grid
where they are neutralized and reflected and from which they travel to 

## Page 55

Vacuum generation
54
2.1.9
Cryopumps
As you may have observed water condenses on cold water mains or
windows and ice forms on the evaporator unit in your refrigerator. This
effect of condensation of gases and vapors on cold surfaces, water vapor in
particular, as it is known in every day life, occurs not only at atmospheric
pressure but also in vacuum.
This effect has been utilized for a long time in condensers (see 2.1.5)
mainly in connection with chemical processes; previously the baffle on
diffusion pumps used to be cooled with refrigerating machines. Also in a
sealed space (vacuum chamber) the formation of condensate on a cold
surface means that a large number of gas molecules are removed from the
volume: they remain located on the cold surface and do not take part any
longer in the hectic gas atmosphere within the vacuum chamber. We then
say that the particles have been pumped and talk of cryopumps when the
“pumping effect” is attained by means of cold surfaces. 
Cryo engineering differs from refrigeration engineering in that the
temperatures involved in cryo engineering are in the range below 120 K 
(< -153 °C). Here we are dealing with two questions:
a) What cooling principle is used in cryo engineering or in cryopumps and
how is the thermal load of the cold surface lead away or reduced?
b) What are the operating principles of the cryopumps?
2.1.9.1 Types of cryopump
Depending on the cooling principle a difference is made between
• Bath cryostats
• Continuous flow cryopumps
• Refrigerator cryopumps
In the case of bath cryostats – in the most simple case a cold trap filled
with LN2 (liquid nitrogen) – the pumping surface is cooled by direct contact
with a liquefied gas. On a surface cooled with LN2 (T ≈ 77 K) H2O and CO2
are able to condense. On a surface cooled to ≈ 10 K all gases except He
and Ne may be pumped by way of condensation. A surface cooled with
liquid helium (T ≈ 4.2 K) is capable of condensing all gases except helium.
In continuous flow cryopumps

## Page 57

Vacuum generation
56
second stage. The attainable low temperatures depend among other things
on the type of regenerator. Commonly copperbronze is used in the
regenerator of the first stage and lead in the second stage. Other materials
are available as regenerators for special applications like cryostats for
extremely low temperatures (T < 10 K). The design of a two-stage cold
head is shown schematically in Fig. 2.67. By means of a control
mechanism with a motor driven control valve (18) with control disk (17) and
control holes first the pressure in the control volume (16) is changed which
causes the displacers (6) of the first stage and the second stage (11)  to
move; immediately thereafter the pressure in the entire volume of the
cylinder is equalized by the control mechanism. The cold head is linked via
flexible pressure lines to the compressor.
2.1.9.3 
The refrigerator cryopump
Fig. 2.68 shows the design of a cryopump. It is cooled by a two-stage cold
head. The thermal radiation shield (5) with the baffle (6) is closely linked
thermally to the first stage (9) of the cold head. For pressures below 
10-3 mbar the thermal load is caused mostly by thermal radiation. For this
reason the second stage (7) with the condensation and cryosorption panels
(8) is surrounded by the thermal radiation shield (5) which is black on the
inside and polished as well as nickel plated on the outside. Under no-load
conditions the baffle and the thermal radiation shield (first stage) attain a
temperature ranging between 50 to 80 K at the cryopanels and about 10 K
at the second stage. The surface temperatures of these cryopanels are
decisive to the actual pumping process. These surface temperatures
depend on the refrigerating power supplied by the cold head, and the
thermal conduction properties in the direction of the pump’s casing. During
operation of the cryopump, loading caused by the gas and the heat of
condensation results in further warming of the cryopanels. The surface
temperatu

## Page 67

66
Vacuum generation
a) the leak rate is extremely small (use of metallic seals), 
b) the gas evolution of the inner surfaces of the vacuum vessel and of the
attached components (e.g., connecting tubulation; valves, seals) can be
made extremely small, 
c) suitable means (cold traps, baffles) are provided to prevent gases or
vapors or their reaction products that have originated from the pumps
used from reaching the vacuum vessel (no backstreaming). 
To fulfill these conditions, the individual components used in UHV
apparatus must be bakeable and extremely leaktight. Stainless steel is the
preferred material for UHV components. 
The construction, start-up, and operation of an UHV system also demands
special care, cleanliness, and, above all, time. The assembly must be
appropriate; that is, the individual components must not be in the least
damaged (i.e. by scratches on precision-worked sealing surfaces).
Fundamentally, every newly-assembled UHV apparatus must be tested for
leaks with a helium leak detector before it is operated. Especially important
here is the testing of demountable joints (flange connections), glass seals,
and welded or brazed joints. After testing, the UHV apparatus must be
baked out. This is necessary for glass as well as for metal apparatus. The
bake-out extends not only over the vacuum vessel, but frequently also to
the attached parts, particularly the vacuum gauges. The individual stages of
the bake-out, which can last many hours for a larger system, and the bake-
out temperature are arranged according to the kind of plant and the
ultimate pressure required. If, after the apparatus has been cooled and the
other necessary measures undertaken (e.g., cooling down cold traps or
baffles), the ultimate pressure is apparently not obtained, a repeated leak
test with a helium leak detector is recommended. Details on the
components, sealing methods and vacuum gauges are provided in our
catalog.
2.3.
Evacuation of a vacuum chamber and
determination of pu

## Page 69

68
2.3.1.2 Evacuation of a chamber in the high vacuum region
It is considerably more difficult to give general formulas for use in the high
vacuum region. Since the pumping time to reach a given high vacuum
pressure depends essentially on the gas evolution from the chamber’s
inner surfaces, the condition and pre-treatment of these surfaces are of
great significance in vacuum technology. Under no circumstances should
the material used exhibit porous regions or – particularly with regard to
bake-out – contain cavities; the inner surfaces must be as smooth as
possible (true surface = geometric surface) and thoroughly cleaned (and
degreased). Gas evolution varies greatly with the choice of material and the
surface condition. Useful data are collected in Table X (Section 9). The gas
evolution can be determined experimentally only from case to case by the
pressure-rise method: the system is evacuated as thoroughly as possible,
and finally the pump and the chamber are isolated by a valve. Now the
time is measured for the pressure within the chamber (volume V) to rise by
a certain amount, for example, a power of 10. The gas quantity Q that
arises per unit time is calculated from:
(2.37)
(Δp = measured pressure rise )
The gas quantity Q consists of the sum of all the gas evolution and all
leaks possibly present. Whether it is from gas evolution or leakage may be
determined by the following method: 
The gas quantity arising from gas evolution must become smaller with time,
the quantity of gas entering the system from leakage remains constant with
time. Experimentally, this distinction is not always easily made, since it
often takes a considerable length of time – with pure gas evolution – before
the measured pressure-time curve approaches a constant (or almost a
constant) final value; thus the beginning of this curve follows a straight line
for long times and so simulates leakage (see Section 5, Leaks and Leak
Detection). 
If the gas evolution Q and the required pressure pend

## Page 71

Vacuum generation
70
of 4 · 10-1 mbar is made with throughput characteristic 2. This corresponds
to the two-stage rotary plunger pump with a nominal pumping speed of 
100 m3/h. Therefore, this pump is the correct backing pump for the 6000 l/s
diffusion pump under the preceding assumption.
However, if the pumping process is such that the maximum throughput of
9.5 mbar · l/s is unlikely, a smaller backing pump can, of course, be used.
This is self-explanatory, for example, from line b in Fig. 2.76 b, which
corresponds to a maximum throughput of only 2 mbar l/s. In this case a 
25 m3/h two-stage rotary-plunger pump would be sufficient. 
2.3.3
Determination of pump-down time from
nomograms
In practice, for instance, when estimating the cost of a planned vacuum
plant, calculation of the pump-down time from the effective pumping speed
Seff, the required pressure p, and the chamber volume V by formulas
presented would be too troublesome and time-consuming. Nomograms are
very helpful here. By using the nomogram in Fig. 9.7 in Section 9, one can
quickly estimate the pump-down time for vacuum plants evacuated with
rotary pumps, if the pumping speed of the pump concerned is fairly
constant through the pressure region involved. By studying the examples
presented, one can easily understand the application of the nomogram. 
The pump-down times of rotary vane and rotary piston pumps, insofar as
the pumping speed of the pump concerned is constant down to the
required pressure, can be determined by reference to example 1.
In general, Roots pumps do not have constant pumping speeds in the
working region involved. For the evaluation of the pump-down time, it
usually suffices to assume the mean pumping speed. Examples 2 and 3 of
the nomogram show, in this context, that for Roots pumps, the compression
ratio K refers not to the atmospheric pressure (1013 mbar), but to the
pressure at which the Roots pump is switched on.
In the medium vacuum region, the gas evolution or the leak rate bec

## Page 87

Vacuum measurement
86
tor and the grid within it as the anode. With this arrangement the electrons
are forced to take very long paths (oscillating around the grid wires of the
anode) so that the probability of ionizing collisions and thus the sensitivity of
the gauge are relatively high. Because the triode system can generally only
be used in high vacuum on account of its strong X-ray effect, the gas sorp-
tion (pumping) effect and the gas content of the electrode system have only
a slight effect on the pressure measurement.
b) The high-pressure ionization vacuum gauge (up to 1 mbar)
A triode is again used as the electrode system (see Fig. 3.16 b), but this
time with an unmodified conventional design. Since the gauge is designed
to allow pressure measurements up to 1 mbar, the cathode must be resis-
tant to relatively high oxygen pressure. Therefore, it is designed as a so-
called non-burnout cathode, consisting of an yttria-coated iridium ribbon. To
obtain a rectilinear characteristic (ion current as a linear function of the
pressure) up to a pressure of 1 mbar, a high-ohmic resistor is installed in
the anode circuit.
c) Bayard-Alpert ionization vacuum gauge (the standard measuring
system used today)
To ensure linearity between the gas pressure and the ion current over as
large a pressure range as possible, the X-ray effect must be suppressed as
far as possible. In the electrode arrangement developed by Bayard and
Alpert, this is achieved by virtue of the fact that the hot cathode is located
outside the anode and the ion collector is a thin wire forming the axis of the
electrode system (see Fig. 3.16 c). The X-ray effect is reduced by two to
three orders of magnitude due to the great reduction in the surface area of
the ion collector. When pressures in the ultrahigh vacuum range are mea-
sured, the inner surfaces of the gauge head and the connections to the ves-
sel affect the pressure reading. The various effects of adsorption, desorp-
tion, dissociation and flow 

## Page 95

Vacuum measurement
94
shown in Fig. 3.31.
Mode of operation: Starting with atmospheric pressure, gas inlet valve V1 is
closed at the beginning of the process. Pump valve V2 opens. The process
chamber is now evacuated until the set pressure, which is preset at the
measuring and switching device, is reached in the process chamber and in
the reference chamber. When the pressure falls below the set switching
threshold, pump valve V2 closes. As a result, the pressure value attained is
“caught” as the reference pressure in the reference chamber (RC) of the
diaphragm controller (DC). Now the process pressure is automatically
maintained at a constant level according to the set reference pressure by
means of the diaphragm controller (DC). If the reference pressure should
rise in the course of the process due to a leak, this is automatically detect-
ed by the measuring and switching device and corrected by briefly opening
pump valve V2. This additional control function enhances the operational
reliability and extends the range of application. Correcting the increased
reference pressure to the originally set value is of special interest for regu-
lated helium circuits because the pressure rise in the reference chamber
(RC) of the diaphragm controller can be compensated for through this
arrangement as a consequence of the unavoidable helium permeability of
the controller diaphragm of FPM.
To be able to change the reference pressure and thus increase the process
pressure to higher pressures, a gas inlet valve must be additionally
installed at the process chamber. This valve is opened by means of a dif-
ferential pressure switch (not shown in Fig. 3.31) when the desired higher
process pressure exceeds the current process pressure by more than the
pressure differential set at the differential pressure switch.

=

## Page 105

Mass spectrometry
104
Type of gas
Symbol
RIP
Type of gas
Symbol
RIP
Acetone (Propanone)
(CH3)2CO
3.6
Hydrogen chloride
HCl
1.6
Air
1.0
Hydrogen fluoride
HF
1.4
Ammonia
NH3
1.3
Hydrogen iodide
HI
3.1
Argon
Ar
1.2
Hydrogen sulfide
H2S
2.2
Benzene
C6H6
5.9
Iodine
I2
Benzoic acid
C6H5COOH
5.5
Krypton
Kr
1.7
Bromine
Br
3.8
Lithium
Li
1.9
Butane
C4H10
4.9
Methane
CH4
1.6
Carbon dioxide
CO2
1.4
Methanol
CH3OH
1.8
Carbon disulfide
CS2
4.8
Neon
Ne
0.23
Carbon monoxide
CO
1.05
Nitrogen
N2
1.0
Carbon tetrachloride
CCl4
6.0
Nitrogen oxide
NO
1.2
Chlorobenzene
C6H4Cl
7.0
Nitrogen dioxide
N2O
1.7
Chloroethane
C2H3Cl
4.0
Oxygen
O2
1.0
Chloroform
CHCl3
4.8
n-pentane
C5H17
6.0
Chlormethane
CH3Cl
3.1
Phenol
C6H5OH
6.2
Cyclohexene
C6H12
6.4
Phosphine
PH3
2.6
Deuterium
D2
0.35
Propane
C3H8
3.7
Dichlorodifluoromethane
CCl2F2
2.7
Silver perchlorate
AgClO4
3.6
Dichloromethane
CH2Cl2
7.8
Tin iodide
Snl4
6.7
Dinitrobenzene
C6H4(NO2)2
7.8
Sulfur dioxide
SO2
2.1
Ethane
C2H6
2.6
Sulfur hexafluoride
SF6
2.3
Ethanol
C2H5OH
3.6
Toluene
C6H5CH3
6.8
Ethylene oxide
(CH2)2O
2.5
Trinitrobenzene
C6H3(NO2)3
9.0
Helium
He
0.14
Water vapor
H2O
11.0
Hexane
C6H14
6.6
Xenon
Xe
3.0
Hydrogen
H2
0.44
Xylols
C6H4(CH3)2
7.8
Table 4.3 Relative ionization probabilities (RIP) vis à vis nitrogen, electron energy 102 eV
Electron energy :
75 eV (PGA 100)
102 eV (Transpector)
Gas
Symbol
Mass
Σ = 100 %
Greatest peak = 100 %
Σ = 100 %
Greatest peak = 100 %
Argon
Ar
40
74.9
100
90.9
100
20
24.7
33.1
9.1
10
36
0.3
Carbon dioxide
CO2
45
0.95
1.3
0.8
1
44
72.7
100
84
100
28
8.3
11.5
9.2
11
16
11.7
16.1
7.6
9
12
6.15
8.4
5
6
Carbon monoxide
CO
29
1.89
2.0
0.9
1
28
91.3
100
92.6
100
16
1.1
1.2
1.9
2
14
1.7
1.9
0.8
12
3.5
3.8
4.6
5
Neon
Ne
22
9.2
10.2
0.9
11
20
89.6
100
90.1
100
10
0.84
0.93
9
4
Oxygen
O2
34
0.45
0.53
32
84.2
100
90.1
100
16
15.0
17.8
9.9
11
Nitrogen
N2
29
0.7
0.8
0.9
1
28
86.3
100
92.6
100
14
12.8
15
6.5
12
Water vapor
H2O
19
1.4
2.3
18
60
100
74.1
100
17
16.1
27
18.5
25
16
1.9
3.2
1.5
2
2
5.0
8.4
1.5
2
1
15.5


## Page 109

Mass spectrometry
108
In the most general case a plurality of gases will make a greater or lesser
contribution to the ion flow for all the masses. The share of a gas g in each
case for the atomic number m will be expressed by the fragment factor
Ffm,g. In order to simplify calculation, the fragment factor Ffm,g will also con-
tain the transmission factor TF and the detection factor DF. Then the ion
current to mass m, as a function of the overall ion currents of all the gases
involved, in matrix notation, is: 
The ion current vector for the atomic numbers m (resulting from the contri-
butions by the fragments of the individual gases) is equal to the fragment
matrix times the vector of the sum of the flows for the individual gases.
or:
(in simplified notation: i = FF · I)
where im
+ = ion flow vector for the atomic numbers, resulting from contribu-
tions of fragments of various individual gases
=  fragment matrix
Ig
+ = Vector of the sum of the flows for the individual gases or:
One sees that the ion flow caused by a gas is proportional to the partial
pressure. The linear equation system can be solved only for the special
instance where m = g (square matrix); it is over-identified for m > g. Due to
unavoidable measurement error (noise, etc.) there is no set of overall ion
flow I+
g (partial pressures or concentrations) which satisfies the equation
system exactly. Among all the conceivable solutions it is now necessary to
identify set I+*
g which after inverse calculation to the partial ion flows I+*
m
will exhibit the smallest squared deviation from the partial ion currents i+
m
actually measured. Thus:
This minimization problem is mathematically identical to the solution of
another equation system
(
)
i
i
m
m
−
=
∑
*
+
+
min
2
Ff m, g

i
p
E
RIP
FF
TF
m
g
N
g
m
m
+ =
⋅
⋅
⋅
⋅
∑
2
Transmission factor
for the mass m
Fragment factor
for the gas to mass m
Relative ionization probability
for the gas
Nitrogen sensitivity (equipment constant)
Partial pressure of th

## Page 111

Leak detection
110
Apart from the vacuum systems themselves and the individual components
used in their construction (vacuum chambers, piping, valves, detachable
[flange] connections, measurement instruments, etc.), there are large num-
bers of other systems and products found in industry and research which
must meet stringent requirements in regard to leaks or creating a so-called
“hermetic” seal. Among these are many assemblies and processes in the
automotive and refrigeration industries in particular but also in many other
branches of industry. Working pressure in this case is often above ambient
pressure. Here “hermetically sealed” is defined only as a relative “absence
of leaks”. Generalized statements often made, such as “no detectable
leaks” or “leak rate zero”, do not represent an adequate basis for accep-
tance testing. Every experienced engineer knows that properly formulated
acceptance specifications will indicate a certain leak rate (see Section 5.2)
under defined conditions. Which leak rate is acceptable is also determined
by the application itself.
5.1
Types of leaks
Differentiation is made among the following leaks, depending on the nature
of the material or joining fault:
• Leaks in detachable connections:
Flanges, ground mating surfaces, covers
• Leaks in permanent connections:
Solder and welding seams, glued joints
• Leaks due to porosity: particularly following mechanical deformation
(bending!) or thermal processing of polycrystalline materials and cast
components
• Thermal leaks (reversible): opening up at extreme temperature loading
(heat/ cold), above all at solder joints
• Apparent (virtual) leaks: quantities of gas will be liberated from hollows
and cavities inside cast parts, blind holes and joints (also due to the
evaporation of liquids)
• Indirect leaks: leaking supply lines in vacuum systems or furnaces
(water, compressed air, brine)
• “Serial leaks”: this is the leak at the end of several “spaces connected in
series”, e.g. a leak in the 

## Page 113

Leak detection
112
5.2.1
The standard helium leak rate
Required for unequivocal definition of a leak are, first, specifications for the 
pressures prevailing on either side of the partition and, secondly, the nature
of the medium passing through that partition (viscosity) or its molar mass.
The designation “helium standard leak” (He Std) has become customary to
designate a situation frequently found in practice, where testing is carried
out using helium at 1 bar differential between (external) atmospheric pres-
sure and the vacuum inside a system (internal, p < 1 mbar), the designa-
tion “helium standard leak rate” has become customary. In order to indicate
the rejection rate for a test using helium under standard helium conditions it
is necessary first to convert the real conditions of use to helium standard
conditions (see Section 5.2.2). Some examples of such conversions are
shown in Figure 5.3.
5.2.2
Conversion equations
When calculating pressure relationships and types of gas (viscosity) it is
necessary to keep in mind that different equations are applicable to laminar
and molecular flow; the boundary between these areas is very difficult to
ascertain. As a guideline one may assume that laminar flow is present at
leak rates where QL > 10-5 mbar · l/s and molecular flow at leak rates
where QL < 10-7 mbar · l/s. In the intermediate range the manufacturer
(who is liable under the guarantee terms) must assume values on the safe
side. The equations are listed in Table 5.2.
Here indices “I” and “II” refer to the one or the other pressure ratio and
indices “1” and “2” reference the inside and outside of the leak point,
respectively.
5.3
Terms and definitions
When searching for leaks one will generally have to distinguish between
two tasks:
1. Locating leaks and
2. Measuring the leak rate.
In addition, we distinguish, based on the direction of flow for the fluid,
between the 
a. vacuum method (sometimes known as an “outside-in leak”), where the
direction of flow is int

## Page 115

Leak detection
114
curve for the rise in pressure must be a straight line where a leak is pre-
sent, even at higher pressures. If the pressure rise is due to gas being lib-
erated from the walls (owing ultimately to contamination), then the pressure
rise will gradually taper off and will approach a final and stable value. In
most cases both phenomena will occur simultaneously so that separating
the two causes is often difficult if not impossible. These relationships are
shown schematically in Figure 5.5. Once it has become clear that the rise
in pressure is due solely to a real leak, then the leak rate can be deter-
mined quantitatively from the pressure rise, plotted against time, in accor-
dance with the following equation:
(5.3)
Example: Once the vacuum vessel with a volume of 20 l has been isolated
from the pump, the pressure in the apparatus rises from 1 · 10-4 mbar to 
1 · 10-3 mbar in 300 s. Thus, in accordance with equation 5.2, the leak rate
will be 
The leak rate, expressed as mass flow Δm / Δt, is derived from equation
5.1 at QL = 6 · 10-5 mbar · l/s, T = 20 °C and the molar mass for air 
(M = 29 g/mole) at
If the container is evacuated with a TURBOVAC 50 turbomolecular pump,
for example (S = 50 l/s), which is attached to the vacuum vessel by way of
a shut-off valve, then one may expect an effective pumping speed of about
Seff = 30 l/s. Thus the ultimate pressure will be 
Q
m
t
mbar
s
g
mol
mol K
mbar
K
g
s
L =
=
⋅
⋅
⋅
⋅
⋅
⋅
⋅
⋅
⋅
⋅
=
⋅
–
–
Δ
Δ
6 10
29
8314
293 10
7 10
5
2
8
ℓ
ℓ
.
QL
mbar
s
=
⋅
–
−⋅
–
⋅
=
⋅
– ⋅
=
–
⋅
⎛
⎝⎜
⎞
⎠⎟
1 10 3
1 10 4
20
300
9 10 4 20
300
6 10 5
⋅
ℓ
QL
p V
t
=
⋅
Δ
Δ
Naturally it is possible to improve this ultimate pressure, should it be insuffi-
cient, by using a larger-capacity pump (e.g. the TURBOVAC 151) and at
the same time to reduce the pump-down time required to reach ultimate
pressure.
Today leak tests for vacuum systems are usually carried out with helium
leak detectors and the vacuum method (see Section 5.7.1). The apparat

## Page 117

Leak detection
116
widely used leak detection methods are shown – together with the test gas,
application range and their particular features – in Table 5.4.
5.5
Leak detectors and how they work
Most leak testing today is carried out using special leak detection devices.
These can detect far smaller leak rates than techniques which do not use
special equipment. These methods are all based on using specific gases
for testing purposes. The differences in the physical properties of these test
gases and the gases used in real-life applications or those surrounding the
test configuration will be measured by the leak detectors. This could, for
example, be the differing thermal conductivity of the test gas and surround-
ing air. The most widely used method today, however, is the detection of
helium used as the test gas.
The function of most leak detectors is based on the fact that testing is con-
ducted with a special test gas, i.e. with a medium other than the one used
in normal operation. The leak test may, for example, be carried out using
helium, which is detected using a mass spectrometer, even though the
component being tested might, for example, be a cardiac pacemaker
whose interior components are to be protected against the ingress of bodily
fluids during normal operation. This example alone makes it clear that the
varying flow properties of the test and the working media need to be taken
into consideration.
5.5.1
Halogen leak detectors 
(HLD 4000, D-Tek)
Gaseous chemical compounds whose molecules contain chlorine and/or
fluorine – such as refrigerants R12, R22 and R134a – will influence the
emissions of alkali ions from a surface impregnated with a mixture of KOH
and Iron(III)hydroxide and maintained at 800 °C to 900 °C by an external
Pt heater. The released ions flow to a cathode where the ion current is
measured and then amplified (halogen diode principle). This effect is so
great that partial pressures for halogens can be measured down to
10-7 mbar.
Whereas suc

## Page 119

Leak detection
118
be continued until all the oil from the pump’s oil pan has been recirculated
several times. This period of time will usually be 20 to 30 minutes.
In order to spare the user the trouble of always having to keep an eye on
the background level, what has been dubbed floating zero-point suppres-
sion has been integrated into the automatic operating concepts of all INFI-
CON leak detectors (Section 5.5.2.5). Here the background level measured
after the inlet valve has been closed is placed in storage; when the valve is
then opened again this value will automatically be deducted from sub-
sequent measurements. Only at a relatively high threshold level will the dis-
play panel show a warning indicating that the background noise level is too
high. Figure 5.8 is provided to illustrate the process followed in zero point
suppression. Chart on the left. The signal is clearly larger than the back-
ground. Center chart: the background has risen considerably; the signal
can hardly be discerned. Chart on the right: the background is suppressed
electrically; the signal can again be clearly identified.
Independent of this floating zero-point suppression, all the leak detectors
offer the capability for manual zero point shifting. Here the display for the
leak detector at the particular moment will be “reset to zero” so that only
rises in the leak rate from that point on will be shown. This serves only to
facilitate the evaluation of a display but can, of course, not influence its
accuracy.
Modern leak detectors are being more frequently equipped with oil-free
vacuum systems, the so-called “dry leak detectors” (UL 200 dry, UL 500
dry). Here the problem of gas being dissolved in oil does not occur but sim-
ilar purging techniques will nonetheless be employed.
5.5.2.3
Calibrating leak detectors; test leaks
Calibrating a leak detector is to be understood as matching the display at a
leak detector unit, to which a test leak is attached, with the value shown on
the “label”

## Page 121

Leak detection
120
sions with neutral gas particles or because their initial energy deviates too
far from the required energy level. These ions are then sorted out by the
suppressor (11) so that only ions exhibiting a mass of 4 (helium) can reach
the ion detector (13). The electron energy at the ion source is 80 eV. It is
kept this low so that components with a specific mass of 4 and higher –
such as multi-ionized carbon or quadruply ionized oxygen – cannot be cre-
ated. The ion sources for the mass spectrometer are simple, rugged and
easy to replace. They are heated continuously during operation and are
thus sensitive to contamination. The two selectable yttrium oxide coated
iridium cathodes have a long service life. These cathodes are largely 
insensitive to air ingress, i.e. the quick-acting safety cut-out will keep them
from burning out even if air enters. However, prolonged use of the ion
source may eventually lead to cathode embrittlement and can cause the
cathode to splinter if exposed to vibrations or shock.
Depending on the way in which the inlet is connected to the mass spec-
trometer, one can differentiate between two types of MSLD.
5.5.2.6
Direct-flow and counter-flow leak detectors
Figure 5.12 shows the vacuum schematic for the two leak detector types. In
both cases the mass spectrometer is evacuated by the high vacuum pump-
ing system comprising a turbomolecular pump and a rotary vane pump. The
diagram on the left shows a direct-flow leak detector. Gas from the inlet
port is admitted to the spectrometer via a cold trap. It is actually equivalent
to a cryopump in which all the vapors and other contaminants condense.
(The cold trap in the past also provided effective protection against the oil
vapors of the diffusion pumps used at that time). The auxiliary roughing
pump system serves to pre-evacuate the components to be tested or the
connector line between the leak detector and the system to be tested. Once
the relatively low inlet pressure (pumping time

## Page 123

122
1. Center: The specimen with volume of V is joined directly with the leak
detector LD (effective pumping speed of S).
2. Left: In addition to 1, a partial flow pump with the same effective pump-
ing speed, Sl = S, is attached to the test specimen.
3. Right: As at 1, but S is throttled down to 0.5◊S.
The signals can be interpreted as follow:
1:  Following a “dead period” (or “delay time”) up to a discernible signal
level, the signal, which is proportional to the partial pressure for helium, will
rise to its full value of pHe = Q/Seff in accordance with equation 5.9:
(5.9 )
The signal will attain a prortion of its ultimate value after 
t = 1 τ . . 63.3 %
t = 2 τ . . 86.5 %
t = 3 τ . . 95.0 %
t = 4 τ . . 98.2 %
t = 5 τ . . 99.3 %
t = 6 τ . . 99.8 %
The period required to reach 95 % of the ultimate value is normally referred
to as the response time.
2:  With the installation of the partial flow pump both the time constant and
the signal amplitude will be reduced by a factor of 2; that means a quicker
rise but a signal which is only half as great. A small time constant means
quick changes and thus quick display and, in turn, short leak detection
times.
3:  The throttling of the pumping speed to 0.5  S, increases both the time
constant and the signal amplitude by a factor of 2. A large value for t thus
increases the time required appropriately. Great sensitivity, achieved by
reducing the pumping speed, is always associated with greater time
requirements and thus by no means is always of advantage.
An estimate of the overall time constants for several volumes connected
one behind to another and to the associated pumps can be made in an ini-
tial approximation by adding the individual time constants.
5.6
Limit values / Specifications for the leak
detector
1. The smallest detectable leak rate.
2. The effective pumping speed at the test connection.
3. The maximum permissible pressure inside the test specimen (also
the maximum permissible inlet pressure). This pressure pma

## Page 125

Leak detection
124
leaking specimens. This procedure is the actual “bombing”. To make the
leak test, then, the specimens are placed in a vacuum chamber following
“bombing”, in the same way as described for the vacuum envelope test.
The overall leak rate is then determined. Specimens with large leaks will,
however, lose their test gas concentration even as the vacuum chamber is
being evacuated, so that they will not be recognized as leaky during the
actual leak test using the detector. It is for this reason that another test to
register very large leaks will have to be made prior to the leak test in the
vacuum chamber.
5.8
Industrial leak testing
Industrial leak testing using helium as the test gas is characterized above
all by the fact that the leak detection equipment is fully integrated into the
manufacturing line. The design and construction of such test units will natu-
rally take into account the task to be carried out in each case (e.g. leak
testing vehicle rims made of aluminum or leak testing for metal drums).
Mass-produced, standardized component modules will be used wherever
possible. The parts to be examined are fed to the leak testing system
(envelope test with rigid envelope and positive pressure [5.7.3.1b] or vacu-
um [5.7.3.2b] inside the specimen) by way of a conveyor system. There
they will be examined individually using the integral methods and automati-
cally moved on. Specimens found to be leaking will be shunted to the side.
The advantages of the helium test method, seen from the industrial point of
view, may be summarized as follows:
• The leak rates which can be detected with this process go far beyond all
practical requirements.
• The integral leak test, i.e. the total leak rate for all individual leaks, facili-
tates the detection of microscopic and sponge-like distributed leaks
which altogether result in leakage losses similar to those for a larger
individual leak.
• The testing procedure and sequence can be fully automated.
• The cyclical,

## Page 173

Statutory units
172
No. Variable
Symbol
SI-
Preferred statutory
No. of remark
Notes
unit
units
in Section 10.3
18
Pressure as mechanical stress
p
N · m–2, Pa
N · mm–2
3/4
19
Diameter
d
m
cm, mm
20
Dynamic viscosity
η (eta)
Pa · s
mPa · s
3/5
21
Effective pressure
pe
N · m–2, Pa
mbar
3/3
see also no. 126
22
Electric field strength
E
V · m–1
V · m–1
23
Electrical capacitance
C
F
F, μF, pF
F = Farad
24
Electrical conductivity
σ (sigma)
S · m–1
S · m–1
25
Electrical conductance
G
S
S
S = Siemens
26
Electrical voltage
U
V
V, mV, kV
27
Electric current density
S
A · m–2
a · m–2, A · cm–2
28
Electric current intensity
I
A
A, mA, μA
29
Electrical resistance
R
Ω (ohm)
Ω, kΩ, MΩ
30
Quantity of electricity (electric charge)
Q
C
C, As
C = Coulomb
31
Electron rest mass
me
kg
kg, g
see Table V in Sect. 9
32
Elementary charge
e
C
C, As
33
Ultimate pressure
pult
N · m–2, Pa
mbar
34
Energy
E
J
J, kJ, kWh, eV
J = Joule
35
Energy dose
D
J · k–1
3/5 a
36
Acceleration of free fall
g
m · s–2
m · s–2
see Table V in Sect. 9
37
Area
A
m2
m2, cm2
38
Area-related impingement rate
ZA
m–2 · s–1
m–2 · s–1; cm–2 · s–1
39
Frequency
f
Hz
Hz, kHz, MHz
40
Gas permeability
Qperm
m3 (NTP)
cm3 (NTP)
3/19
d =day (see Tab. 10.4.4
––––––––––
––––––––––
m2 · s · Pa
m2 · d · bar
see no. 73 and no. 103)
41
Gas constant
R
42
Velocity
v
m · s–1
m · s–1, mm · s–1, km · h–1
43
Weight (mass)
m
kg
kg, g, mg
3/6
44
Weight (force)
G
N
N, kN
3/7
45
Height
h
m
m, cm, mm
46
Lift
s
m
cm
see also no. 139
47
Ion dose
J
C · kg–1
c · kg–1, C · g–1
3/8
48
Pulse
p^ (b)
N · s
N · s
49
Inductance
L
H
H, mH
H = Henry
50
Isentropic exponent
κ (kappa)
–
–
κ = cp · cv
–1
51
Isobaric molar heat capacity
Cmp
J · mol–1 · K–1 J · mol–1 · K–1
52
Isobaric specific heat capacity
cp
J · kg–1 · K–1
J · kg–1 · K–1
53
Isochore molar heat capacity
Cmv
J · mol–1 · K–1
54
Isochore specific heat capacity
cv
J · kg–1 · K–1
J · kg–1 · K–1
55
Kinematic viscosity
ν (nü)
m2 · s–1
mm2 · s–1, cm2 · s–1
3/9
56
Kinetic energy
EK
J
J
57
Force
F
N
N, kN, mN


## Page 181

180
DIN
Title
Issue
55350
Definitions of quality assurance and statistics
Part 11 – Basic definitions of quality assurance
8/95
Part 18 – Definitions regarding certification of 
results of quality tests/quality test certificates
7/87
66038
Torr – millibar; millibar – torr conversion tables
4/71
–
Thesaurus Vacui (definition of terms)
1969
A)   European/national agreements, EN, DIN/EN, CEN 
DIN/EN
Title
Issue
EN 473
Training and certification of personnel for 
nondestructive testing (including leak test)
7/93
837-1
Pressure gauges, Part 1: Pressure gauges with 
Bourdon tubes, dimensions, measurement 
technology, requirements and testing
2/97
837-2
Pressure gauges, Part 2: Selection and installation 
recommendations for pressure gauges
1/95
837-3
Pressure gauges, Part 3: Pressure gauges with 
plate and capsule elements, dimensions, 
measurement technology, requirements 
and testing
2/97
1330-8 E Nondestructive testing - definitions for leak test – 
terminology
6/94
1779 E
Nondestructive testing – leak test. Instructions 
for selection of a testing method
3/95
1338-8 E Nondestructive testing – leak test. 
Terminology on leak test
1994
1518 E
Nondestructive testing – determination of 
characteristic variables for mass spectrometer 
leak detectors
1593 E
Nondestructive testing – bubble type testing method 12/94
NMP 826 Calibration of gaseous reference leaks, CD
9/95
Nr. 09–95
B)   International agreements, ISO, EN/ISO 
ISO
Title
Issue
1000
SI units and recommendations for the use of 
their multiples and of certain other units
11/92
1607 / 1
Positive displacement vacuum pumps.
Measurement of performance characteristics.
12/93
Part 1 - Measurement of volume rate of flow
(pumping speed)
ISO
Title
Issue
1607 / 2
Positive displacement vacuum pumps. 
Measurement of performance characteristics.
11/89
Part 2 - Measurement of ultimate pressure
1608 / 1
Vapor vacuum pumps. 
Part 1: Measurement ofvolume rate of flow
12/93
1608 / 2
Vapor vacuum pumps. 
Part 2: Measurement of critica

## Page 193

192
K. H. Behrndt and R. W. Love
Automatic control of Film Deposition Rate with the crystal oscillator for
preparation of alloy films.
Vacuum 12 ,1-9, 1962
P. Lostis
Automatic Control of Film Deposition Rate with the Crystal Oscillator for
Preparation fo Alloy Films.
Rev. Opt. 38, 1 (1959)
K. H. Behrndt
Longterm operation of crystal oscillators in thin film deposition 
J. Vac. Sci. Technol. 8, 622 (1971)
L. Wimmer, S. Hertl, J. Hemetsberger and E. Benes
New method of measuring vibration amplitudes of quartz crystals. 
Rev. Sci. Instruments 55 (4) , 608, 1984
P. J. Cumpson and M. P. Seah
Meas. Sci. Technol., 1, 548, 1990
J. G. Miller and D. I. Bolef
Sensitivity Enhancement by the use of Acoustic Resonators in cw
Ultrasonic Spectroscopy.
J. Appl. Phys. 39, 4589, (1968)
J. G. Miller and D. I. Bolef
Acoustic Wave Analysis of the Operation of Quartz Crystal Film Thickness
Monitors.
J. Appl. Phys. 39, 5815, (1968)
C. Lu and O. Lewis
Investigation of Film thickness determination by oscillating quartz res-
onators with large mass load.
J. Appl. Phys. 43, 4385 (1972)
C. Lu
Mas determination with piezoelectric quartz crystal resonators.
J. Vac. Sci. Technol. Vol. 12 (1), 581-582, 1975
A. Wajid
U.S. Patent No. 505,112,642 (May 12, 1992)
C. Hurd
U.S. Patent No. 5,117,192 (May 26, 1992)
E. Benes
Improved Qartz Crystal Microbalance Technique
J. Appl. Phys. 56, (3), 608-626 (1984)
C. J. Wilson
Vibration modes of AT-cut convex quartz resonators.
J. Phys. d 7, 2449, (1974)
H. F. Tiersten and R. C. Smythe
An analysis of contowced crystal resonators operating in overtones of cou-
pled thickness shear and thickness twist.
J. Acoustic Soc. Am. 65, (6) 1455, 1979
R. E. Bennett, C. Rutkoeski and L. A. Taylor
Proceedings of the Thirteenth Annual Symposium on Frequency Controll,
479, 1959 
Chih-shun Lu
Improving the accuracy of Quartz csystal monitors
Research/Development, Vol. 25, 45-50, 1974, Technical Publishing
Company
A. Wajid
Improving the accuracy of a quartz crystal microbalance wit

## Page 195

194
13. Index 
Absolute pressure  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9
Absorption isotherms  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .50
Absorption pumps  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .50, 144
Absorption traps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .38
Accessories for rotary displacement pumps  . . . . . . . . . . . . . . . . . . . . . . .38
Active oscillator  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .127, 128
Adjustment and calibration of vacuum gauges  . . . . . . . . . . . . . . . . . . . . .86
Adsorption pumps,Instructions for operation  . . . . . . . . . . . . . . . . . .144, 145
Aggressive vapors  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .140
AGM (aggressive gas monitor)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .99
Air, atmospheric  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .13
ALL·ex pumps  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .32, 35
Ambient pressure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9
Amonton's law  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .13
Anticreep barrier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .45
Anti-suckback valve  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .22
APIEZON AP 201  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .44, 166
Atmospheric air  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .13
Atmospheric air, composition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .150
Atmospheric pressur

## Page 197

196
MEMBRANOVAC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .78
Mercury (pump fluid) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .41, 44,166
Mode-lock oscillator  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .128
Molar gas constant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9, 14, 148
Molar mass (molecular weight)  . . . . . . . . . . . . . . . . . . . . . . . . . . . .9, 12, 13
Molecular flow  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .15
Molecular sieve  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .50, 145
Monolayer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .12
Monolayer formation time  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .12, 16, 65
National standards, resetting to  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .86
NEG pumps (non evaporable getter pumps)  . . . . . . . . . . . . . . . . . . .50, 53
Neoprene  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .73, 154, 155, 156
Nitrogen equivalent  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .76, 83
Nominal internal diameter and internal diameter of tubes . . . . . . . . . . . .151
Nomogram  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .70
Nomogram: conductance of tubes / entire pressure range  . . . . . . . . . . .164
Nomogram: conductance of tubes / laminar flow range  . . . . . . . . . . . . .161
Nomogram: conductance of tubes / molecular flow range  . . . . . . .161, 163
Nomogram: pump down time / medium vacuum, taking in 
account the outgasing from the walls  . . . . . . . . . . . . . . . . . . . . . . . . . . .165
Nomogram: pump down time / rough vacuum . . . . . . . . . . . . . . . . . . . . .162
N

