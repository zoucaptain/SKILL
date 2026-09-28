# Vacuum Basics (Leybold)

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

## Page 15

Vacuum physics
14
Model concepts and basic assumptions:
1. Atoms/molecules are points.
2. Forces are transmitted from one to another only by collision.
3. The collisions are elastic.
4. Molecular disorder (randomness) prevails.
A very much simplified model was developed by Krönig. Located in a cube
are N particles, one-sixth of which are moving toward any given surface of
the cube. If the edge of the cube is 1 cm long, then it will contain n particles
(particle number density); within a unit of time n · c · Δt/6 molecules will
reach each wall where the change of pulse per molecule, due to the
change of direction through 180 °, will be equal to 2 · mT · c. The sum of
the pulse changes for all the molecules impinging on the wall will result in a
force effective on this wall or the pressure acting on the wall, per unit of
surface area.
where
Derived from this is
Ideal gas law (derived from the kinetic gas theory)
If one replaces c2 with c2– then a comparison of these two “general” gas
equations will show:
or
The expression in brackets on the left-hand side is the Boltzmann constant
k; that on the right-hand side a measure of the molecules’ mean kinetic
energy:
Boltzmann constant
Mean kinetic energy of the molecules
thus
In this form the gas equation provides a gas-kinetic indication of the tem-
perature!
p V
N k T
N E kin
·
=
· ·
=
·
·
2
3
E kin
mT c
=
·
2
2
k
mT R
M
J
K
=
·
=
−
138 10 23
.
·
p V
N
mT R
M
T
N
mT c
·
=
·
·
·
=
·
·
·
(
)
(
)
2
3
2
2
p V
m
M R T
N mT c
·
=
·
·
=
·
·
·
1
3
2
p V
N mT c
·
=
·
·
·
1
3
2
n
N
V
=
n c
mT c
n c
mT
p
6
2
1
3
2
· · ·
· =
· ·
·
=
The mass of the molecules is
where NA is Avogadro’s number (previously: Loschmidt number).
Avogadro constant 
NA = 6.022 ⋅1023 mol–1
For 1 mole, 
and
V = Vm = 22.414 l (molar volume); 
Thus from the ideal gas law at standard conditions 
(Tn = 273.15 K and pn = 1013.25 mbar):
For the general gas constant:
1.4 
The pressure ranges in vacuum technology
and their characterization
(See also Table IX in Chapter 

## Page 17

16
“group velocity” and is not identical with the “thermal velocity” of the gas
molecules.
In the molecular flow range, on the other hand, impact of the particles with
the walls predominates. As a result of reflection (but also of desorption fol-
lowing a certain residence period on the container walls) a gas particle can
move in any arbitrary direction in a high vacuum; it is no longer possible to
speak of ”flow” in the macroscopic sense.
It would make little sense to attempt to determine the vacuum pressure
ranges as a function of the geometric operating situation in each case. The
limits for the individual pressure regimes (see Table IX in Chapter 9) were
selected in such a way that when working with normal-sized laboratory
equipment the collisions of the gas particles among each other will predom-
inate in the rough vacuum range whereas in the high and ultrahigh vacuum
ranges impact of the gas particles on the container walls will predominate.
In the high and ultrahigh vacuum ranges the properties of the vacuum con-
tainer wall will be of decisive importance since below 10–3 mbar there will
be more gas molecules on the surfaces than in the chamber itself. If one
assumes a monomolecular adsorbed layer on the inside wall of an evacuat-
ed sphere with 1 l volume, then the ratio of the number of 
adsorbed particles to the number of free molecules in the space will be as
follows:
at 1
mbar
10–2
at 10–6
mbar
10+4
at 10–11
mbar
10+9
For this reason the monolayer formation time τ (see Section 1.1) is used to
characterize ultrahigh vacuum and to distinguish this regime from the high
vacuum range. The monolayer formation time τ is only a fraction of a sec-
ond in the high vacuum range while in the ultrahigh vacuum range it
extends over a period of minutes or hours. Surfaces free of gases can
therefore be achieved (and maintained over longer periods of time) only
under ultrahigh vacuum conditions.
Further physical properties change as pressure changes. For example, the
the

## Page 29

28
one’s consideration on the cold state. The smallest clearances and thus the
lowest back flows are attained at operating pressures in the region of 
1 mbar. Subsequently it is possible to attain in this region the highest
compression ratios, but this pressure range is also most critical in view of
contacts between the rotors and the casing.
Characteristic quantities of roots pumps
The quantity of gas Qeff effectively pumped by a Roots pump is calculated
from the theoretically pumped quantity of gas Qth and the internal leakage
QiR (as the quantity of gas which is lost) as:
Qeff = Qth – QiR
(2.5)
The following applies to the theoretically pumped quantity of gas:
Qth = pa · Sth
(2.6)
where pa is the intake pressure and Sth is the theoretical pumping speed.
This in turn is the product of the pumping volume VS and the speed n:
Sth = n · VS
(2.7)
Similarly the internal leakage QiR is calculated as:
QiR = n · ViR
(2.8)
where pV is the forevacuum pressure (pressure on the forevacuum side)
and SiR is a (notional) “reflow” pumping speed with
SiR = n · ViR
(2.9)
i.e. the product of speed n and internal leakage volume ViR.
Volumetric efficiency of a Roots pumps is given by
(2.10)
By using equations 2.5, 2.6, 2.7 and 2.8 one obtains
(2.11)
When designating the compression pv/pa as k one obtains
(2.11a)
Maximum compression is attained at zero throughput (see PNEUROP and
DIN 28 426, Part 2). It is designated as k0:
(2.12)
k0 is a characteristic quantity for the Roots pump which usually is stated as
a function of the forevacuum pressure pV (see Fig. 2.18). k0 also depends
(slightly) on the type of gas.
For the efficiency of the Roots pump, the generally valid equation applies:
(2.13)
η = −
1
k
ko
k
S
S
th
iR
0
0
=
=
(
)η
η = −
1 k S
S
iR
th
η = −
·
1
p
p
S
S
V
a
iR
th
η = Q
Q
eff
th
Normally a Roots pump will be operated in connection with a downstream
rough vacuum pump having a nominal pumping speed SV. The continuity
equation gives:
SV · pV = Seff · pa = η · Sth · pa
(2.14)
Fr

## Page 39

Vacuum generation
38
2.1.4
Accessories for oil-sealed rotary
displacement pumps
During a vacuum process, substances harmful to rotary pumps can be
present in a vacuum chamber.
Elimination of water vapor
Water vapor arises in wet vacuum processes. This can cause water to be
deposited in the inlet line. If this condensate reaches the inlet port of the
pump, contamination of the pump oil can result. The pumping performance
of oil-sealed pumps can be significantly impaired in this way. Moreover,
water vapor discharged through the outlet valve of the pump can condense
in the discharge outlet line. The condensate can, if the outlet line is not
correctly arranged, run down and reach the interior of the pump through the
discharge outlet valve. Therefore, in the presence of water vapor and other
vapors, the use of condensate traps is strongly recommended. If no
discharge outlet line is connected to the gas ballast pump (e.g., with
smaller rotary vane pumps), the use of discharge filters is recommended.
These catch the oil mist discharged from the pump.
Some pumps have easily exchangeable filter cartridges that not only hold
back oil mist, but clean the circulating pump oil. Whenever the amount of
water vapor present is greater than the water vapor tolerance of the pump,
a condenser should always be installed between the vessel and the pump.
(For further details, see Section 2.1.5)
Elimination of dust
Solid impurities, such as dust and grit, significantly increase the wear on
the pistons and the surfaces in the interior of the pump housing. If there is
a danger that such impurities can enter the pump, a dust separator or a
dust filter should be installed in the inlet line of the pump. Today not only
conventional filters having fairly large casings and matching filter inserts
are available, but also fine mesh filters which are mounted in the centering
ring of the small flange. If required, it is recommended to widen the cross
section with KF adaptors.
Elimination of oil vapor 

## Page 41

Vacuum generation
40
necessary. However, if the condenser is small, the opposite case arises:
pv2 > pS · pp2, is small. Here a relatively large gas ballast pump is required.
Since the quantity of air involved during a pumping process that uses
condensers is not necessarily constant but alternates within more or less
wide limits, the considerations to be made are more difficult. Therefore, it is
necessary that the pumping speed of the gas ballast pump effective at the
condenser can be regulated within certain limits. 
In practice, the following measures are usual:
a) A throttle section is placed between the gas ballast pump and the
condenser, which can be short-circuited during rough pumping. The flow
resistance of the throttle section must be adjustable so that the effective
speed of the pump can be reduced to the required value. This value can
be calculated using the equations given in Section 2.2.3.
b) Next to the large pump for rough pumping a holding pump with low
speed is installed, which is of a size corresponding to the minimum
prevailing gas quantity. The objective of this holding pump is merely to
maintain optimum operating pressure during the process.
c) The necessary quantity of air is admitted into the inlet line of the pump
through a variable-leak valve. This additional quantity of air acts like an
enlarged gas ballast, increasing the water vapor tolerance of the pump.
However, this measure usually results in reduced condenser capacity.
Moreover, the additional admitted quantity of air means additional power
consumption and (see Section 8.3.1.1) increased oil consumption. As
the efficiency of the condenser deteriorates with too great a partial
pressure of air in the condenser, the admission of air should not be in
front, but generally only behind the condenser.
If the starting time of a process is shorter than the total running time,
technically the simplest method – the roughing and the holding pump – is
used. Processes with strongly varying conditions

## Page 43

Vacuum generation
42
chosen backing pump must be such (see 2.3.2) that the amount of gas
discharged from the diffusion pump is pumped off without building up a
backing pressure that is near the maximum backing pressure or even
exceeding it. 
The attainable ultimate pressure depends on the construction of the pump,
the vapor pressure of the pump fluid used, the maximum possible
condensation of the pump fluid, and the cleanliness of the vessel.
Moreover, backstreaming of the pump fluid into the vessel should be
reduced as far as possible by suitable baffles or cold traps (see Section
2.1.6.4).
Degassing of the pump oil
In oil diffusion pumps it is necessary for the pump fluid to be degassed
before it is returned to the boiler. On heating of the pump oil, decomposition
products can arise in the pump. Contamination from the vessel can get into
the pump or be contained in the pump in the first place. These constituents
of the pump fluid can significantly worsen the ultimate pressure attainable
by a diffusion pump, if they are not kept away from the vessel. Therefore,
the pump fluid must be freed of these impurities and from absorbed gases. 
This is the function of the degassing section, through which the circulating
oil passes shortly before re-entry into the boiler. In the degassing section,
the most volatile impurities escape. Degassing is obtained by the carefully
controlled temperature distribution in the pump. The condensed pump fluid,
which runs down the cooled walls as a thin film, is raised to a temperature
of about 130 °C below the lowest diffusion stage, to allow the volatile
components to evaporate and be removed by the backing pump. Therefore,
the re-evaporating pump fluid consists of only the less volatile components
of the pump oil.
Pumping speed
The magnitude of the specific pumping speed S of a diffusion pump – that
is, the pumping speed per unit of area of the actual inlet surface – depends
on several parameters, including the position and dimensions of 

## Page 45

44
2.1.6.3
Pump fluids
a) Oils
The suitable pump fluids for oil diffusion pumps are mineral oils, silicone
oils, and oils based on the polyphenyl ethers. Severe demands are placed
on such oils which are met only by special fluids. The properties of these,
such as vapor pressure, thermal and chemical resistance, particularly
against air, determine the choice of oil to be used in a given type of pump
or to attain a given ultimate vacuum. The vapor pressure of the oils used in
vapor pumps is lower than that of mercury. Organic pump fluids are more
sensitive in operation than mercury, because the oils can be decomposed
by long-term admission of air. Silicone oils, however, withstand longer
lasting frequent admissions of air into the operational pump.
Typical mineral oils are DIFFELEN light, normal and ultra. The different
types of DIFFELEN are close tolerance fractions of a high quality base
product (see our catalog).
Silicone oils (DC 704, DC 705, for example) are uniform chemical
compounds (organic polymers). They are highly resistant to oxidation in the
case of air inrushes and offer special thermal stability characteristics.
DC 705 has an extremely low vapor pressure and is thus suited for use in
diffusion pumps which are used to attain extremely low ultimate pressures
of < 10-10 mbar.
ULTRALEN is a polyphenylether. This fluid is recommended in all those
cases where a particularly oxidation-resistant pump fluid must be used and
where silicone oils would interfere with the process.
APIEZON AP 201 is an oil of exceptional thermal and chemical resistance
capable of delivering the required high pumping speed in connection with
oil vapor ejector pumps operating in the medium vacuum range. The
attainable ultimate total pressure amounts to about 10-4 mbar.
b) Mercury
Mercury is a very suitable pump fluid. It is a chemical element that during
vaporization neither decomposes nor becomes strongly oxidized when air
is admitted. However, at room temperature it has a comparative

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

## Page 61

Vacuum generation
60
(small cryopanels compared to a large wall surface) is often not true,
because large cryopanels are required to attain short pumpdown times and
a good end vacuum. Deviations also result when the cryopanels are
surrounded by a cooled baffle at which the velocity of the penetrating
molecules is already reduced by cooling.
Service life / duration of operation top (s): The duration of operation of
the cryopump for a particular gas depends on the equation:
with
CG =
Capacity of the cryopump for the gas G
QG(t) = Throughput of the cryopump for the gas at the point of time t
If the constant mean over time for the throughput QG
__
is known, the
following applies:
(2.30)
After the period of operation top,G has elapsed the cryopump must be
regenerated with respect to the type of gas G.
Starting pressure po: Basically it is possible to start a cryopump at
atmospheric pressure. However, this is not desirable for several reasons.
As long as the mean free path of the gas molecules is smaller than the
dimensions of the vacuum chamber (p > 10-3 mbar), thermal conductivity of
the gas is so high that an unacceptably large amount of heat is transferred
to the cryopanels. Further, a relatively thick layer of condensate would form
on the cryopanel during starting. This would markedly reduce the capacity
of the cryopump available to the actual operating phase. Gas (usually air)
would be bonded to the adsorbent, since the bonding energy for this is
lower than that for the condensation surfaces. This would further reduce
the already limited capacity for hydrogen. It is recommended that
cryopumps in the high vacuum or ultrahigh vacuum range are started with
the aid of a backing pump at pressures of p < 5 · 10-2 mbar. As soon as the
starting pressure has been attained the backing pump may be switched off.
t
C
Q
C
p
S
op G
G
G
G
G
G
, =
=
·
C
Q t dt
G
G
top G
= ∫
( )
,
0
2.2
Choice of pumping process 
2.2.1
Survey of the most usual pumping
processes 
Vacuum technology has

## Page 63

62
2.2.2
Pumping of gases (dry processes)
For dry processes in which a non condensable gas mixture (e.g., air) is to
be pumped, the pump to be used is clearly characterized by the required
working pressure and the quantity of gas to be pumped away. The choice
of the required working pressure is considered in this section. The choice of
the required pump is dealt with in Section 2.3. 
Each of the various pumps has a characteristic working range in which it
has a particularly high efficiency. Therefore, the most suitable pumps for
use in the following individual pressure regions are described. For every
dry-vacuum process, the vessel must first be evacuated. It is quite possible
that the pumps used for this may be different from those that are the
optimum choices for a process that is undertaken at definite working
pressures. In every case the choice should be made with particular
consideration for the pressure region in which the working process
predominantly occurs.
a) Rough vacuum (1013 – 1 mbar)
The usual working region of the rotary pumps described in Section 2 lies
below 80 mbar. At higher pressures these pumps have a very high power
consumption (see Fig. 2.11) and a high oil consumption (see Section
8.3.1.1). Therefore, if gases are to be pumped above 80 mbar over long
periods, one should use, particularly on economic grounds, jet pumps,
water ring pumps or dry running, multi-vane pumps. Rotary vane and rotary
piston pumps are especially suitable for pumping down vessels from
atmospheric pressure to pressures below 80 mbar, so that they can work
continuously at low pressures. If large quantities of gas arise at inlet
pressures below 40 mbar, the connection in series of a Roots pump is
recommended. Then, for the backing pump speed required for the process
concerned, a much smaller rotary vane or piston pump can be used. 
b) Medium vacuum (1 – 10-3 mbar)
If a vacuum vessel is merely to be evacuated to pressures in the medium
vacuum region, perhaps to that of the 

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

## Page 77

Vacuum measurement
76
3.
Vacuum measurement, monitoring, control
and regulation
The pressures measured in vacuum technology today cover a range from
1013 mbar to 10-12 mbar, i.e. over 15 orders of magnitude. The enormous
dynamics involved here can be shown through an analogy analysis of vacu-
um pressure measurement and length measurement, as depicted in Table
3.1.
Analogy analysis
Determination by
Absolute
means of
pressure
Length
empirical world
of human beings
1 bar
1 m
simple measuring 
methods
> 1 mbar
> 1 mm
mechanical
measuring 
methods
> 10–3 mbar
> 1 mm
indirect 
methods
10–9 mbar
≈1/100 atom∅
extreme indirect 
≈0.18
methods
10–12 mbar
electron∅
Table 3.1
Measuring instruments designated as vacuum gauges are used for mea-
surement in this broad pressure range. Since it is impossible for physical
reasons to build a vacuum gauge which can carry out quantitative measure-
ments in the entire vacuum range, a series of vacuum gauges is available,
each of which has a characteristic measuring range that usually extends over
several orders of magnitude (see Fig. 9.16a). In order to be able to allocate
the largest possible measuring ranges to the individual types of vacuum
gauges, one accepts the fact that the measurement uncertainty rises very
rapidly, by up to 100 % in some cases, at the upper and lower range limits.
This interrelationship is shown in Fig. 3.1 using the example of the VISCO-
VAC. Therefore, a distinction must be made between the measuring range
as stated in the catalogue and the measuring range for “precise” measure-
ment. The measuring ranges of the individual vacuum gauges are limited in
the upper and lower range by physical effects.
3.1
Fundamentals of low-pressure measure-
ment
Vacuum gauges are devices for measuring gas pressures below atmos-
pheric pressure (DIN 28 400, Part 3, 1992 issue). In many cases the pres-
sure indication depends on the nature of the gas. With compression vacu-
um gauges it should be noted that if vapors are present, 

## Page 83

Vacuum measurement
82
With other electrical measuring methods that are dependent on the type 
of gas, the particle number density is measured indirectly by means of 
the amount of heat lost through the particles (thermal conductivity vacuum
gauge) or by means of the number of ions formed (ionization vacuum
gauge).
3.3.2
Thermal conductivity vacuum gauges
Classical physics teaches and provides experimental confirmation that the
thermal conductivity of a static gas is independent of the pressure at higher
pressures (particle number density), p > 1 mbar. At lower pressures, 
p < 1 mbar, however, the thermal conductivity is pressure-dependent
(approximately proportional 1 / 
M). It decreases in the medium vacuum
range starting from approx. 1 mbar proportionally to the pressure and
reaches a value of zero in the high vacuum range. This pressure depen-
dence is utilized in the thermal conductivity vacuum gauge and enables
precise measurement (dependent on the type of gas) of pressures in the
medium vacuum range.
The most widespread measuring instrument of this kind is the Pirani vacu-
um gauge. A current-carrying filament with a radius of r1 heated up to
around 100 to 150 °C (Fig. 3.10) gives off the heat generated in it to the
gas surrounding it through radiation and thermal conduction (as well as, of
course, to the supports at the filament ends). In the rough vacuum range
the thermal conduction through gas convection is virtually independent of
pressure (see Fig. 3.10). If, however, at a few mbar, the mean free path of
the gas is of the same order of magnitude as the filament diameter, this
type of heat transfer declines more and more, becoming dependent on the
density and thus on the pressure. Below 10-3 mbar the mean free path of a
gas roughly corresponds to the size of radius r2 of the measuring tubes.
The sensing filament in the gauge head forms a branch of a Wheatstone
bridge. In the THERMOTRON thermal conductivity gauges with variable
resistance which were commo

## Page 85

Vacuum measurement
84
gettering surface film on the walls of the gauge tube. In spite of these dis-
advantages, which result in a relatively high degree of inaccuracy in the
pressure reading (up to around 50 %), the cold-cathode ionization gauge
has three very outstanding advantages. First, it is the least expensive of all
high vacuum measuring instruments. Second, the measuring system is
insensitive to the sudden admission of air and to vibrations; and third, the
instrument is easy to operate.
3.3.3.2
Hot-cathode ionization vacuum gauges
Generally speaking, such gauges refer to measuring systems consisting of
three electrodes (cathode, anode and ion collector) where the cathode is a
hot cathode. Cathodes used to be made of tungsten but are now usually
made of oxide-coated iridium (Th2O3, Y2O3) to reduce the electron output
work and make them more resistant to oxygen. Ionization vacuum gauges
of this type work with low voltages and without an external magnetic field.
The hot cathode is a very high-yield source of electrons. The electrons are
accelerated in the electric field (see Fig. 3.13) and receive sufficient energy
from the field to ionize the gas in which the electrode system is located. The
positive gas ions formed are transported to the ion collector, which is nega-
tive with respect to the cathode, and give up their charge there. The ion cur-
rent thereby generated is a measure of the gas density and thus of the gas
pressure. If i- is the electron current emitted by the hot cathode, the pres-
sure-proportional current i+ produced in the measuring system is defined by:
i+ = C · i– · p und
(3.3)
(3.3a)
The variable C is the vacuum gauge constant of the measuring system. 
p
i
i
C
=
⋅
+
−
For nitrogen this variable is generally around 10 mbar-1. With a constant
electron current the sensitivity S of a gauge head is defined as the quotient
of the ion current and the pressure. For an electron current of 1 mA and C
= 10 mbar-1, therefore, the sensitivity S of the g

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

## Page 93

Vacuum measurement
92
To achieve higher flow rates, several diaphragm controllers can be connect-
ed in parallel. This means that the process chambers and the reference
chambers are also connected in parallel. Fig. 3.29 shows such a connection
of 3 MR 50 diaphragm controllers.
To control a vacuum process, it is frequently necessary to modify the pres-
sure in individual process steps. With a diaphragm controller this can be
done either manually or via electric control of the reference pressure.
Electric control of the reference pressure of a diaphragm controller is rela-
tively easy because of the small reference volume that always remains con-
stant. Fig. 3.31 shows such an arrangement on the left as a picture and on
the right schematically, see 3.5.5 for application examples with 
diaphragm controllers.
To be able to change the reference pressure and thus the process pressure
towards higher pressures, a gas inlet valve must additionally be installed at
the process chamber. This valve is opened by means of a differential pres-
sure switch (not shown in Fig. 3.31) when the desired higher process pres-
sure exceeds the current process pressure by more than the pressure dif-
ference set on the differential pressure switch.
3.5.4
Pressure regulation in high and ultrahigh
vacuum systems
If the pressure is to be kept constant within certain limits, an equilibrium
must be established between the gas admitted to the vacuum vessel and
the gas simultaneously removed by the pump with the aid of valves or throt-
tling devices. This is not very difficult in rough and medium vacuum sys-
tems because desorption of adsorbed gases from the walls is generally
negligible in comparison to the quantity of gas flowing through the system.
Pressure regulation can be carried out through gas inlet or pumping speed
regulation. However, the use of diaphragm controllers is only possible
between atmospheric pressure and about 10 mbar.
In the high and ultrahigh vacuum range, on the other hand, t

## Page 97

Mass spectrometry
96
4.3
The quadrupole mass spectrometer
(TRANSPECTOR)
The ion beam extracted from the electron impact ion source is diverted into
a quadrupole separation system containing four rod-shaped electrodes. The
cross sections of the four rods form the circle of curvature for a hyperbola
so that the surrounding electrical field is nearly hyperbolic. Each of the two
opposing rods exhibits equal potential, this being a DC voltage and a super-
imposed high-frequency AC voltage (Fig. 4.2). The voltages applied induce
transverse oscillations in the ions traversing the center, between the rods.
The amplitudes of almost all oscillations escalate so that ultimately the ions
will make contact with the rods; only in the case of ions with a certain ratio
of mass to charge m/e is the resonance condition which allows passage
through the system satisfied. Once they have escaped from the separation
system the ions move to the ion trap (detector, a Faraday cup) which may
also take the form of a secondary electron multiplier pick-up (SEMP). 
The length of the sensor and the separation system is about 15 cm. To
ensure that the ions can travel unhindered from the ion source to the ion
trap, the mean free path length inside the sensor must be considerably
greater than 15 cm. For air and nitrogen, the value is about 
p · λ = 6 · 10–3 mbar · cm. At p = 1 · 10-4 bar this corresponds to a mean
free path length of λ = 60 cm. This pressure is generally taken to be the
minimum vacuum for mass spectrometers. The emergency shut-down fea-
ture for the cathode (responding to excessive pressure) is almost always
set for about 5 · 10-4 mbar. The desire to be able to use quadrupole spec-
trometers at higher pressures too, without special pressure convertors, led
to the development of the XPR sensor at INFICON (XPR standing for
extended pressure range). To enable direct measurement in the range of
about 2 · 10-2 mbar, so important for sputter processes, the rod system was
reduced from 12 cm

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

## Page 149

Tables, Formulas, Diagrams
148
Table IV:  Compilation of important formulas pertaining to the kinetic theory of gases
8 ⋅R ⋅T

π ⋅M
T 
cm
M  
s
2 ⋅R ⋅T

M
Variable
Most probable speed
of particles cw
Mean velocity
of particles c–
Mean square of velocity
of particles c2–
Gas pressure p of particles
Number density of particles n
Area-related impingement ZA
Volume collision rate ZV
Equation of state of ideal gas
Area-related mass flow rate qm, A
c* =λ · p in cm · mbar
λ
mean free path in cm
NA Avogadro constant in mol–1
p
gas pressure in mbar
T
thermodynamic temperature in K
(see Tab. III)
M
molar mass in g · mol–1
n
number density of particles in cm–3
R molar gas constant
V volume in l
k
Boltzmann constant in mbar · l · K–1
mT particle mass in g
ν
amount of substance in mol
in mbar · l · mol–1 K–1
General formula
p = n ⋅k ⋅T
1
p = ⋅n ⋅mT ⋅c2
–
3
1
p = ⋅ϱ ⋅c2
–
3
1
ZV = ⋅n ⋅c–
2
λ
1
ZA = 
⋅p2
c*
p = 13.80 ⋅10–20 ⋅n ⋅T [mbar]
p = 4.04 ⋅10–17 ⋅n [mbar] (applies to all gases)
p = 2.5 ⋅1016 ⋅p [cm–3] (applies to all gases)
ZA = 2.85 ⋅1020 ⋅p [cm–2 s–1] (see Fig. 78.2)
ZV = 8.6 ⋅1022 ⋅p2 [cm–3 s–1] (see Fig. 78.2)
p ⋅V = 2.44 ⋅104 ν [mbar ⋅ℓ] (for all gases)
p ⋅V = 83.14 ⋅ν ⋅T [mbar ⋅ℓ]
Qm, A = 4.377 ⋅10–2
⋅p [g cm–2 s–1]
p ⋅V = ν ⋅R ⋅T
qm, A = ZA ⋅mT =
⋅p
n = p/kT
qm, A = 1.38 ⋅10–2 ⋅p g [cm–2 s–1]
For easy calculation
Value for air at 20°C
cw =
cw = 1.29 ⋅104
cw = 410 [m/s]
c– =
c2
– =
c2
– = 2.49 ⋅108
c2
– = 25.16 ⋅104
c– = 1.46 ⋅104
c– = 464 [m/s]
T
cm2
M
s2
cm2
s2
3 ⋅R ⋅T
M
T 
cm
M  
s
M
T
M

2 ⋅π ⋅k ⋅T ⋅NA
NA

2 ⋅π ⋅M ⋅k ⋅T
2 ⋅NA

π ⋅M ⋅k ⋅T
p
n = 7.25 ⋅1018 ⋅
[cm–3]
T
p
ZA = 2.63 · 1022 ·
· p [cm–2 s–1]

M · T

p2
ZV = 5.27 · 1022 ·
[cm–3 s–1]
c*· 

M
· T
1
ZA = · n · c–
4
ZA =
· p
Table V: Important values
Designation,
Symbol
Value and
Remarks
alphabetically
unit
Atomic mass unit
mu
1.6605 · 10–27 kg
Avogadro constant
NA
6.0225 · 1023 mol–1
Number of particles per mol,
formerly: Loschmidt number
Boltzmann constant
k
1.3805 

## Page 151

Tables, Formulas, Diagrams
150
% by weight
% by volume
Partial pressure mbar
N2
75.51
78.1
792
O2
23.01
20.93
212
Ar
1.29
0.93
9.47
CO2
0.04
0.03
0.31
Ne
1.2 · 10–3
1.8 · 10–3
1.9 · 10–2
He
7 · 10–5
7 · 10–5
5.3 · 10–3
CH4
2 · 10–4
2 · 10–4
2 · 10–3
Kr
3 · 10–4
1.1 · 10–4
1.1 · 10–3
N2O
6 · 10–5
5 · 10–5
5 · 10–4
H2
5 · 10–6
5 · 10–5
5 · 10–4
Xe
4 · 10–5
8.7 · 10–6
9 · 10–5
O3
9 · 10–6
7 · 10–6
7 · 10–5
Σ 100 %
Σ 100 %
Σ 1013
50 % RH at 20 °C
1.6
1.15
11.7
Note: In the composition of atmospheric air the relative humidity (RH) is indicated separately along with the temperature.
At the given relative humidity, therefore, the air pressure read on the barometer is 1024 mbar.
Table VIII: Composition of atmospheric air
Rough vacuum
Medium vacuum
High vacuum
Ultrahigh vacuum
Pressure
p [mbar]
1013 – 1
1 – 10–3
10–3 – 10–7
< 10–7
Particle number density
n [cm–3]
1019 – 1016
1016 – 1013
1013 – 109
< 109
Mean free path 
λ [cm]
< 10–2
10–2 – 10
10 – 105
> 105
Impingement rate
Za [cm–2 · s–1]
1023 – 1020
1020 – 1017
1017 – 1013
< 1013
Vol.-related collision rate
ZV [cm–3 · s–1]
1029 – 1023
1023 – 1017
1017 – 109
< 109
Monolayer time
τ [s]
< 10–5
10–5 – 10–2
10–2 – 100
> 100
Type of gas flow
Viscous flow
Knudsen flow
Molecular flow
Molecular flow
Other special features
Convection dependent
Significant change in
Significant reduction-
Particles on the 
on pressure
thermal conductivity 
in volume
surfaces dominate
of a gas
related collision rate
to a great extend in 
relation to particles in 
gaseous space
Table IX: Pressure ranges used in vacuum technology and their characteristics (numbers rounded off to whole power of ten)
At room temperature
Standard values1
Metals
Nonmetals
(mbar · l · s–1 · cm–2)
10–9 ... · 10–7
10–7 ... · 10–5
Outgassing rates (standard values) as a function of time
Examples:
1/2 hr.
1 hr.
3 hr.
5 hr.
Examples:
1/2 hr.
1 hr.
3 hr.
5 hr.
Ag
1.5 · 10–8
1.1 · 10–8
2 · 10–9
Silicone
1.5 · 10–5
8 · 10–6
3.5 · 10–6
1.5 · 10–6
Al
2 · 10–8
6 · 10–9
NBR
4 · 10–6
3 ·

## Page 161

Tables, Formulas, Diagrams
160
Kelvin
Celsius
Réaumur Fahrenheit Rankine
Boiling point H2O
373
100
80
212
672
Body temperature 37°C
310
37
30
99
559
Room temperature
293
20
16
68
527
Freezing point H2O
273
0
0
32
492
NaCl/H2O 50:50
255
–18
–14
0
460
Freezing point Hg
34
–39
–31
–39
422
CO2 (dry ice)
195
–78
–63
–109
352
Boiling point LN2
77
–196
–157
–321
170
Absolute zero point
0
–273
–219
–460
0
Table XVII:  Temperature comparison and conversion table (rounded off to whole degrees)
K
Kelvin
°C
Celsius
°C
Réaumur
°F
Fahrenheit
°R
Rankine
K
°C
°R
°F
°R
Kelvin
Celsius
Réaumur
Fahrenheit
Rankine
1
K – 273
(K – 273)
(K – 273) + 32
K = 1,8 K
°C + 273
1
· °C
· °C + 32
(°C + 273)
· °R + 273
· °R
1
· °R + 32
(°R + 273)
(°F – 32) + 273
(°F – 32)
(°F – 32)
1
°F + 460
(°R)
(°R – 273)
(°R – 273)
°R – 460
1
4
5
9
5
9
5
9
5
9
5
4
5
5
4
5
4
5
9
5
9
5
9
5
9
4
9
4
5
5
9
9
4
5
9
5
4
[          ]
[          ]
Fig. 9.1:
Variation of mean free path λ (cm) with pressure for various gases
Pressure p [mbar]
Mean free path λ [cm]
Fig. 9.2:
Diagram of kinetics of gases for air at 20 °C
λ
: mean free path in cm (λ ~ 1/p)
n
: particle number density in cm–3 (n ~ p)
ZA : area-related impingement rate in cm–3 · s–1 (ZA ~ p2)
ZV : volume-related collision rate in cm–3 · s–1 (ZV ~ p2)
1
λ~ p
Pressure p [mbar]
ZA – p2
ZV – p2
Conversion in

=

## Page 163

Tables, Formulas, Diagrams
162
Fig. 9.7:
Nomogram for determination of pump-down time tp of a vessel in the rough vacuum pressure range
pEND – pend, p
mbar
Column ¿ : Vessel volume V in liters
Column ¡ : Maximum effective pumping speed Seff,max at the
vessel in (left) liters per second or (right) cubic
meters per hour.
Column ¬ : Pump-down time tp in (top right) seconds or (cen-
ter left) minutes or (bottom right) hours.
Column √: Right:
Pressure pEND in millibar at the END of the pump-
down time if the atmospheric pressure 
pSTART ( pn = 1013 prevailed at the START of the
pump-down time. The desired pressure pEND is to
be reduced by the ultimate pressure of the pump
pult,p and the differential value is to be used in the
columns. If there is inflow qpV,in, the value 
pend – pult,p – qpV,in / Seff,max is to be used in the
columns.
Left:
Pressure reduction ratio R = (pSTART – pult,p –
qpV,in / Seff,max)/(pend – pult,p – qpV,in / Seff,max), if
the pressure pSTART prevails at the beginning of
the pumping operation and the pressure is to be
lowered to pEND by pumping down.
The pressure dependence of the pumping speed
is taken into account in the nomogram and is
expressed in column ƒ by pult,p. If the pump
pressure pult,p is small in relation to the pressure
pend which is desired at the end of the pump-
down operation, this corresponds to a constant
pumping speed S or Seff during the entire pump-
ing process.
Example 1 with regard to nomogram 9.7:
A vessel with the volume V = 2000 l  is to be pumped down
from a pressure of pSTART = 1000 mbar (atmospheric pres-
sure) to a pressure of pEND = 10-2 mbar by means of a rotary
plunger pump with an effective pumping speed at the vessel of
Seff,max = 60 m3/h = 16.7 l · s-1. The pump-down time can be
obtained from the nomogram in two steps:
1) Determination of τ: A straight line is drawn through 
V = 2000 l (column ¿ ) and Seff = 60 m3/h-1 = 16.7 l · s-1 (col-
umn ¡ ) and the value t = 120 s = 2 min is read off at the
intersection 

## Page 169

Tables, Formulas, Diagrams
168
Ultrahigh vacuum
<10–7 mbar
<10–5 Pa
High vacuum
10–7 to 10–3 mbar
10–5 to 10–1 Pa
Medium vacuum
10–3 to 1 mbar
10–1 to 102 Pa
Rough vacuum
1 to approx. 103 mbar
102 to approx. 105 Pa
Fig. 9.16a: Measurement ranges of common vacuum gauges
10–13
10–12
10–11
10–10
10–9
10–8
10–7
10–6
10–5
10–4
10–3
10–2
10–1
100
101
102
Pressure balance
Bourdon vacuum gauge
Liquid level vacuum gauge
(McLeod vacuum gauge)
Decrement vacuum gauge
Pirani vacuum gauge
Thermal conductivity vacuum gauge
Compression vacuum gauge
Cold-cathode ionization vacuum gauge
Penning ionization vacuum gauge
Hot-cathode ionization vacuum gauge
103
10–14
p in mbar →
Working range for special models or special operating data
Diaphragm vacuum gauge
Capacitance diaphragm vacuum gauge
Piezoelectric vacuum gauge
U-tube vacuum gauge
Thermocouple vacuum gauge
Bimetallic vacuum gauge
Thermistor vacuum gauge
Magnetron gauge
Triode ionization vacuum gauge for medium vacuum
Triode ionization vacuum gauge for high vacuum
Bayard-Alpert ionization vacuum gauge
Bayard-Alpert ionization vacuum gauge with modulator
Extractor vacuum gauge
Partial pressure vacuum gauge
The customary limits are indicated in the diagram.
Spring element vacuum gauge

=

## Page 189

188
M. H. Hablanian
Backstreaming Measurements above Liquid-Nitrogen Traps 
Vac. Sci. Tech., Vol. 6, 265-268, 1969
Z. Hulek, Z. Cespiro, R. Salomonovic, M. Setvak and J. Voltr
Measurement of oil deposit resulting from backstreaming in a diffusion
pump system by proton elastic scattering
Vacuum, Vol. 41 (7-9), 1853-1855, 1990
M. H. Hablanian
Elimination of backstreaming from mechanical vacuum pumps
J. Vac. Sci. Technol. A5 (4), 1987, 2612-2615
3.
Ultrahigh vacuum technology
G. Kienel
Probleme und neuere Entwicklungen auf dem Ultrahochvakuum-Gebiet 
VDI-Zeitschrift, 106, 1964, 777-786
G. Kienel und E. Wanetzky
Eine mehrmals verwendbare Metalldichtung für ausheizbare
Uktrahochvakuum-Ventile und Flanschdichtungen
Vakuum-Technik, 15, 1966, 59-61
H. G. Nöller
Physikalische und technische Voraussetzungen für die Herstellung und
Anwendung von UHV-Geräten.
„Ergebnisse europäischer Ultrahochvakuum Forschung“
LEYBOLD-HERAEUS GmbH u. Co., in its own publishing house, Cologne
1968, 49-58
W. Bächler
Probleme bei der Erzeugung von Ultrahochvakuum mit modernen Vakuum-
pumpen. „Ergebnisse europäischer Ultrahochvakuum Forschung“
Leybold-Heraeus GmbH u. Co., in its own publishing house, Cologne 1968, 
139-148
P. Readhead, J. P. Hobson und E. V. Kornelsen
The Physical Basis of Ultrahigh Vacuum
Chapman and Hall, London, 1968
E. Bergandt und H. Henning
Methoden zur Erzeugung von Ultrahochvakuum
Vakuum-Technik, 25,1970, 131-140
H. Wahl
Das Hochvakuumsystem der CERN am 450 GeV Supersynchrotron und
Speichering (SPS)
Vakuum in der Praxis, 1989, 43-51
F. Grotelüschen
Das UHV-System bei DESY. 1. Teil
Vakuum in der Praxis, 4, 1991, 266-273
D. Trines
Das Strahlrohrvakuumsystem des Hera-Protonenringes
Vakuum in der Praxis, 2, 1992, 91-99 
G. Schröder et al.
COSV- eine neue Forschungsanlage mit UHV-Technologie
Vakuum in der Praxis, 5, 1993, 229-235
W. Jacobi
Das Vakuumsystem der GSI-Beschleunigeranlage
Vakuum in der Praxis, 6, 1994, 273-281
4.
Conductances, flanges, 
valves, etc. 
M. Knudsen
Geset

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

