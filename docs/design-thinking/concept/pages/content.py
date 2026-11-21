# All page copy for the Hyped Up site concept, written from the content model (content-model.md) in Hypa's voice.
# One source of truth: hubs, footer and menus are generated from GROUPS, so a hub always lists every footer service.
# Prices: "from £" only, from memory/price-list-master.md, then memory/pricing.md. Anything unconfirmed is listed in TBC.
# Photos: file names in img/ (see docs/design-build/media-log.md); None = honest "photo needed" block.

GROUPS = [
    ('security', 'Security', ['ghost-immobiliser', 'car-trackers', 'dash-cams', 'car-alarms', 'taxi-cameras']),
    ('upgrades', 'Upgrades', ['carplay', 'car-audio', 'remapping', 'reverse-cameras', 'ambient-lighting', 'performance-parts']),
    ('styling', 'Styling', ['car-wrapping', 'paint-protection-film', 'window-tinting', 'air-suspension', 'coilovers', 'chrome-delete',
                            'bodykits', 'wheel-refurb', 'interiors', 'detailing', 'number-plates', 'van-signage']),
]
MENU = {'security': ['ghost-immobiliser', 'car-trackers', 'dash-cams'],
        'upgrades': ['carplay', 'car-audio', 'remapping'],
        'styling': ['car-wrapping', 'paint-protection-film', 'window-tinting', 'air-suspension']}

S = {}
def svc(slug, **k): S[slug] = k

# ---------------- SECURITY ----------------
svc('ghost-immobiliser', group='security', name='Ghost immobiliser', short='Ghost & immobilisers', chip='security',
    title='Ghost Immobiliser Fitting in South London | Hyped Up',
    desc='Ghost immobiliser fitted in Bermondsey, South London, from £400. A PIN on your car\'s own buttons stops relay theft and cloned keys. Cars and motorbikes.',
    img='alfa-keys-wheel.jpg', alt='Steering wheel buttons, start button and keys', price='from £400',
    line='No PIN, no start. Relay kits and cloned keys get nothing.',
    lead="Ghost II works through your car's own CAN bus and locks the engine out until you enter a PIN on buttons the car already has: steering wheel, windows, doors. No fob to clone, no signal to relay, no box for a thief to find.",
    price_note='Fitted, with your PIN set up and the car fully tested. The exact price depends on the car.',
    options=[('Ghost II', 'PIN on the steering wheel, window or door buttons. Invisible, no LED, no fob. Cars and motorbikes.'),
             ('Metablok and Metablok-e', 'A tag in your pocket instead of a PIN; the e version adds app control. From £495.'),
             ('Scorpion X-series', 'Immobiliser that works with Scorpion tracking and alarms. From £495.'),
             ('OBD port protection', 'Stops thieves plugging into the diagnostic port to code a new key. Usually fitted alongside. <span class="tbc">(TBC: Hypa)</span>')],
    steps=[('Get in', 'Unlock the car as normal with your own key.'), ('Enter your PIN', 'A short sequence on buttons the car already has. Only you know it.'),
           ('Drive', 'No PIN, no start, even with the key in the car.')],
    faq=[('Can thieves bypass a Ghost?', 'There\'s no fob to clone and no signal to relay, and it isn\'t reached through the OBD port, so the usual tools don\'t work. Nothing is unbeatable, so for a high-value car we\'d pair it with a tracker.'),
         ('How long does fitting take?', 'About 2–3 hours, depending on the car.'),
         ('Ghost, Metablok or Scorpion?', 'Ghost uses a PIN; Metablok and Scorpion use a tag or app. All three stop the car starting. Tell us how you use the car and we\'ll say which suits you.'),
         ('Does it work on motorbikes?', 'Yes, we fit Ghost to cars and motorcycles.'),
         ('Will my insurer recognise it?', 'Many insurers ask about immobilisers; check your policy. We give you the paperwork after fitting. <span class="tbc">(Wording TBC: Hypa)</span>')],
    makes=[('Range Rover', '#'), ('BMW', '#'), ('Mercedes', '#')], related=['car-trackers', 'car-alarms', 'dash-cams'],
    blog=[('Ghost immobiliser: cost, fitting and is it worth it?', '#')])

svc('car-trackers', group='security', name='Car trackers', short='Car trackers', chip='security',
    title='Car Tracker Fitting in London: S5 & S7 Trackers | Hyped Up',
    desc='GPS car trackers fitted in Bermondsey, South London, from £395: S7 and S5 trackers with 24/7 monitoring and battery backup, plus motorbike trackers.',
    img='tracker.jpg', alt='MetaTrak tracker card in front of a Mercedes in the workshop', price='from £395',
    line='Live location and a 24/7 monitoring centre, if it goes anyway.',
    lead="S5 or S7, hidden where thieves don't look. The second the car or bike moves without you, the alert goes out, the monitoring centre follows it and helps the police get it back.",
    price_note='Plus a monthly monitoring subscription on most trackers. We\'ll tell you which, and how much, before you book.',
    options=[('S7 trackers (SmartTrack Trident)', 'Live GPS, 24/7 monitoring centre, battery backup. Alerts if the car moves or the battery is cut.'),
             ('S5 trackers (MetaTrak, Scorpion)', 'Everything S7 does, plus a driver tag: if the car moves without it, the alert goes out straight away.'),
             ('Motorbike trackers (Datatool S5)', 'Small unit hidden under the seat or in the tail.')],
    steps=[('Pick the tracker', 'S7, S5 or bike: we\'ll match it to the car and to what your insurer asks for.'), ('Hidden fitting', 'Wired in where a thief won\'t look, tested before you leave.'), ('Live on your phone', 'App set up with you; the monitoring centre knows your car.')],
    good='Some insurers ask for a specific tracker category. Send us your policy wording and we\'ll match it. <span class="tbc">(Thatcham / insurer wording TBC: Hypa)</span>',
    faq=[('S5 or S7: what\'s the difference?', 'Both track live with 24/7 monitoring and battery backup. S5 adds a driver tag, so it knows when the car moves without you.'),
         ('Is there a monthly fee?', 'Yes, for monitored trackers. We\'ll give you the exact figure before you book.'),
         ('Is an AirTag enough?', 'It helps find lost things, but it has no monitoring centre, no battery backup in the car and thieves scan for them. A fitted tracker is hidden and watched 24/7.'),
         ('Do you fit trackers to bikes?', 'Yes, compact S5 trackers built for motorcycles.')],
    related=['ghost-immobiliser', 'car-alarms', 'dash-cams'], blog=[('Why every London car owner needs security right now', '#')])

svc('dash-cams', group='security', name='Dash cams', short='Dash cams', chip='security',
    title='Dash Cam Installation in London: Front & Rear | Hyped Up',
    desc='Dash cams hardwired in Bermondsey, South London, from £125: front, front and rear or 3-channel, with parking mode. FineVu and Thinkware, or the one you own.',
    img='dashcam.jpg', alt='Dash cam fitted behind the mirror of a BMW', price='from £125',
    line='Front, rear or 3-channel, hardwired, with parking mode.',
    lead="Footage wins arguments. We hardwire front, rear and 3-channel cams so they record every drive and keep watching while the car's parked, with every wire hidden in the trim.",
    price_note='Fitting from £125 for one camera, more for two or three channels. Supply and fit from FineVu, or we fit the camera you already have.',
    options=[('Front', 'Records the road ahead.'), ('Front and rear', 'Covers the most common claims: shunts and cash-for-crash.'),
             ('3-channel', 'Adds an inside camera: taxis, private hire and delivery.'), ('Parking mode', 'Wakes on a knock while parked, with battery protection so it won\'t flatten the car.')],
    steps=[('Choose the setup', '1, 2 or 3 cameras, bring your own or supplied.'), ('Hardwired neatly', 'Wiring hidden in the trims, no cables hanging.'), ('Set up with you', 'App, parking mode and footage saving shown before you leave.')],
    faq=[('Can you fit a dash cam I already bought?', 'Yes, we hardwire existing cameras.'),
         ('Will parking mode drain my battery?', 'Not when it\'s fitted with a voltage cut-off, which is how we do it.'),
         ('Which dash cam do you recommend?', 'For most cars a front and rear camera with GPS and parking mode. We stock FineVu and fit Thinkware too.'),
         ('Do you fit dash cams to taxis?', 'Yes. For licensed taxis and PHVs see TfL taxi cameras.')],
    related=['taxi-cameras', 'car-trackers', 'reverse-cameras'], blog=[('Best dash cam 2026: front, rear and GPS', '#')])

svc('car-alarms', group='security', name='Car alarms', short='Car alarms', chip='security',
    title='Car Alarm Fitting & Repair in London | Hyped Up',
    desc='Car alarms fitted and fixed in Bermondsey, South London: Scorpion alarms with tilt, shock and glass-break sensors and phone alerts. Alarm keeps going off? Talk to us.',
    img='audi-r8-unit.jpg', alt='Black Audi R8 outside the Hyped Up unit', price='price on enquiry',
    line='Tilt, shock and glass-break sensors, with the alert on your phone.',
    lead='A siren on its own gets ignored on a London street. A modern alarm reads tilt, shock and glass-break sensors and sends the alert straight to your phone.',
    price_note='Price depends on the car and the alarm. <span class="tbc">(Price TBC: Hypa)</span>',
    options=[('Scorpion alarms', 'Shock, tilt and glass-break sensors, app arm and disarm, tamper alerts.'), ('Motorbike alarms', 'Loud siren with motion and shock sensors.'),
             ('Alarm keeps going off?', 'Usually a sensor set too high or a weak battery. We check it and fix or replace it. <span class="tbc">(TBC: Hypa)</span>')],
    steps=[('Tell us the car', 'And whether it\'s a new alarm or a fault.'), ('Fit or fix', 'Sensors set for where you park.'), ('Phone alerts', 'App set up with you.')],
    faq=[('Are car alarms still worth it?', 'On their own, less than they were. Paired with an immobiliser and a tracker they warn you early, which is the point.'),
         ('Why does my car alarm keep going off?', 'Most often a sensitive sensor, a weak battery or a door or bonnet switch. It\'s usually a quick fix.'),
         ('Do you fit alarms to bikes?', 'Yes.')],
    related=['ghost-immobiliser', 'car-trackers', 'dash-cams'], blog=[])

svc('taxi-cameras', group='security', name='Taxi cameras (TfL)', short='Taxi cameras (TfL)', chip='security',
    title='TfL Approved Taxi Cameras Fitted in London | Hyped Up',
    desc='TfL-approved camera systems fitted for London black cabs and private hire, from £395: 2SeeTV, HikVision and ACSS, installed and tested in Bermondsey.',
    img='wrap.jpg', alt='London taxi in the Hyped Up workshop', price='from £395',
    line='TfL-approved camera systems for black cabs and private hire.',
    lead="TfL-approved camera systems for licensed taxis and private hire. Wired in, tested and set up to TfL's rules, so you're covered.",
    price_note='2-channel approved systems from £395 supplied and fitted.',
    options=[('2SeeTV and HikVision 2-channel', 'Approved systems for black cabs and PHVs.'), ('ACSS EC2', 'Approved alternative system.'), ('Install only', 'Already bought an approved system? We fit it.')],
    steps=[('Check your licence type', 'Taxi or PHV, and what TfL asks for.'), ('Fit and test', 'Cameras, recorder and signage.'), ('Paperwork', 'What you need for your records.')],
    good='Only approved systems meet TfL rules. We\'ll confirm the right one for your licence. <span class="tbc">(Wording TBC: Hypa)</span>',
    faq=[('Which taxi camera is TfL approved?', 'We fit approved systems including 2SeeTV, HikVision and ACSS. Tell us your vehicle and licence and we\'ll confirm.'),
         ('Can you fit a camera I bought?', 'Yes, install only is available.')],
    related=['dash-cams', 'car-trackers'], blog=[])

# ---------------- UPGRADES ----------------
svc('carplay', group='upgrades', name='CarPlay & Android Auto', short='CarPlay & Android Auto', chip='screens',
    title='Apple CarPlay Installation in London | Hyped Up',
    desc='Apple CarPlay and Android Auto fitted in Bermondsey, South London, from £170: new screens or wireless CarPlay on your factory screen, steering controls kept.',
    img='audi-r8-carplay.jpg', alt='Audi R8 dashboard with a new CarPlay screen', price='from £170',
    line='Wireless CarPlay on a new screen or your factory one.',
    lead='Wireless CarPlay and Android Auto, with your steering wheel controls still working. A new screen, or an interface behind the factory one so the dash still looks stock.',
    price_note='From £170 for a double DIN head unit; interfaces for factory screens cost more. <span class="tbc">(Which price table is current: Hypa)</span>',
    options=[('New screen', 'Xtrons or Autostyle screens made for your car, or Pioneer and Kenwood double DIN.'), ('Keep your factory screen', 'A CarPlay interface behind the dash: looks standard, works wireless.'),
             ('Add a reverse camera', 'Goes straight into the new screen.')],
    steps=[('Send us your car and year', 'We check what fits and keeps your controls.'), ('Fitted', 'Screen or interface, wired and set up.'), ('Paired with your phone', 'Shown working before you leave.')],
    faq=[('Will CarPlay work in my car?', 'Most cars from about 2008 can have it, either with a new screen or an interface on the factory one. Send us the make, model and year.'),
         ('Will my steering wheel controls still work?', 'Yes, we keep them working.'), ('Wireless or wired?', 'Wireless on most setups.'),
         ('Do you do Android Auto too?', 'Yes, the same screens do both.')],
    makes=[('BMW', '#'), ('Mini', '#'), ('Mercedes', '#'), ('Audi', '#')], related=['reverse-cameras', 'car-audio', 'dash-cams'],
    blog=[('Apple CarPlay installation in South London', '#')])

svc('car-audio', group='upgrades', name='Car audio', short='Car audio', chip='screens',
    title='Car Audio Upgrades in London: Speakers, Subs | Hyped Up',
    desc='Car audio upgrades in Bermondsey, South London, from £125: speakers, amps, subwoofers, sound deadening and custom boot builds. Rockford Fosgate fitted properly.',
    img='boot-build.jpg', alt='Custom boot build with a red and black subwoofer enclosure', price='from £125',
    line='Speakers, amps, subs, sound deadening and boot builds.',
    lead='Door speakers, amps, subs, sound deadening and full custom boot builds. We deaden the doors first, because a good speaker in a rattling door is wasted money.',
    price_note='Door speakers from £125 · mono amp and sub from £225 · sound deadening from £145 a door · custom boot builds quoted per car.',
    options=[('Speakers', 'Clearer sound from the doors, the cheapest big upgrade.'), ('Amps and subwoofers', 'Bass you can feel, without rattles. Rockford Fosgate.'),
             ('Sound deadening', 'Quieter cabin and tighter bass, per door or full floor.'), ('Custom boot builds', 'Enclosures, Alcantara, LED: built for shows.')],
    steps=[('Tell us what you listen to', 'And your budget.'), ('Built and fitted', 'Wiring done properly, no rattles.'), ('Tuned to the car', 'Set up and played with you.')],
    faq=[('Can I keep my factory head unit?', 'Yes, with a line driver or an amp that takes the factory signal.'), ('How much is a full system?', 'It depends on the car and what you want; send us both and we\'ll price it.'),
         ('Do you upgrade BMW speakers?', 'Yes, BMW speaker upgrades are one of the most common jobs.')],
    makes=[('BMW', '#')], related=['carplay', 'ambient-lighting', 'reverse-cameras'], blog=[('Car audio upgrade: subs, amps and lighting', '#')])

svc('remapping', group='upgrades', name='Remapping', short='Remapping', chip='remap',
    title='Car Remapping in London: Stage 1, 2 & 3 | Hyped Up',
    desc='ECU remapping in Bermondsey, South London: Stage 1, 2 and 3 for cars and motorbikes, done safely with KESS3 and JB4. Honest advice on MOT and insurance.',
    img='remap.jpg', alt='Mercedes in the workshop with remapping kit', price='from £250',
    line="Stage 1 to 3, cars and bikes, mapped for the hardware you've got.",
    lead='More power and sharper response, without cooking the engine. We read the ECU, check the car is healthy first, then map it for the hardware it actually has. Cars and motorbikes.',
    price_note='Stage 1 from £250. Stage 2 and 3 depend on the hardware. <span class="tbc">(Prices TBC: Hypa; live site says £435 / mobile £199)</span>',
    options=[('Stage 1', 'Software only, on a standard car.'), ('Stage 2', 'With supporting parts such as intake and exhaust.'), ('Stage 3', 'Bigger hardware changes, quoted per build.'), ('Motorbike remaps', 'Same care, for bikes.')],
    steps=[('Health check', 'We read the ECU and check the car before touching it.'), ('Map', 'Written for your car and fuel, using KESS3 or JB4.'), ('Test drive', 'Checked on the road with you.')],
    good='Tell your insurer about a remap. Some changes, like removing a catalytic converter or DPF, will fail an MOT and aren\'t road legal: we won\'t do those for road cars.',
    faq=[('Is remapping safe?', 'Done properly on a healthy car, yes. That\'s why we check the car first.'), ('Do I need to tell my insurer?', 'Yes, always.'),
         ('Will it pass the MOT?', 'A sensible remap on a car with its emissions parts in place, yes.'), ('Do you remap motorbikes?', 'Yes.')],
    related=['performance-parts', 'air-suspension', 'car-audio'], blog=[('ECU remapping: more power, safely', '#'), ('Car tuning in London: how to pick a safe tuner', '#')])

svc('reverse-cameras', group='upgrades', name='Reverse cameras & parking sensors', short='Reverse cameras & sensors', chip='screens',
    title='Reverse Camera & Parking Sensor Fitting London | Hyped Up',
    desc='Reverse cameras and parking sensors fitted in Bermondsey, South London, from £125. For cars, vans and work vehicles, into your screen or a mirror monitor.',
    img=None, need='a reverse camera on a screen', alt='', price='from £125',
    line='Cameras from £125, sensors from £295.',
    lead='Park without guessing. Cameras into your screen or a mirror monitor, sensors front or rear, on cars and vans.',
    price_note='Camera fitting from £125 · rear sensors from £295 · front sensors from £350.',
    options=[('Reverse camera', 'Into a CarPlay screen, factory screen or mirror monitor.'), ('Rear parking sensors', 'Colour-matched, beeps as you get close.'), ('Front parking sensors', 'For tight London parking.'), ('Vans and work vehicles', 'Cameras and sensors for fleets.')],
    steps=[('Tell us the car', 'And which screen it has.'), ('Fitted and colour-matched', 'Sensors painted to match where needed.'), ('Tested with you', 'Guidelines set up on screen.')],
    faq=[('Can you add a camera to my factory screen?', 'On many cars, yes, with an interface. Send us the model.'), ('Do you fit sensors to vans?', 'Yes.')],
    related=['carplay', 'dash-cams'], blog=[])

svc('ambient-lighting', group='upgrades', name='Ambient lighting & starlights', short='Ambient lighting & starlights', chip='screens',
    title='Ambient Lighting & Starlight Headliners London | Hyped Up',
    desc='Ambient interior lighting, starlight headliners, door shadow lights and under-car lighting fitted in Bermondsey, South London, from £160.',
    img='abarth-ambient.jpg', alt='Abarth interior lit with purple ambient lighting', price='from £160',
    line='Ambient strips, starlights, door and under-car lights.',
    lead='Ambient strips, door shadow lights, under-car glow and full starlight headliners, with every fibre placed by hand.',
    price_note='Door shadow lights from £160 a pair · ambient lighting from £445 · starlight headliners from £795 · under-car lighting from £380.',
    options=[('Ambient lighting', 'Strips in the dash and doors, colour from your phone.'), ('Starlight headliner', 'Hundreds of fibre-optic stars in the roof.'),
             ('Door shadow lights', 'Your logo on the ground when the door opens.'), ('Under-car lighting', 'For shows.')],
    steps=[('Pick the look', 'Colour, zones, effects.'), ('Fitted cleanly', 'No visible wires.'), ('Set up on your phone', 'Shown before you leave.')],
    good='Coloured lights showing outside the car can be illegal on the road; under-car lighting is for shows. <span class="tbc">(Wording TBC: Hypa)</span>',
    faq=[('How long does a starlight headliner take?', 'Usually a full day or more, depending on the car. <span class="tbc">(TBC)</span>'), ('Can I change colours?', 'Yes, from an app on most kits.')],
    related=['car-audio', 'interiors', 'carplay'], blog=[])

svc('performance-parts', group='upgrades', name='Exhausts & performance parts', short='Exhausts & performance parts', chip='remap',
    title='Exhausts & Performance Parts Fitted in London | Hyped Up',
    desc='Exhausts, intakes and performance parts fitted in Bermondsey, South London, to go with a remap or on their own. Road-legal advice, cars and motorbikes.',
    img='mini-jcw-show.jpg', alt='Mini JCW at a show with the bonnet open', price='price on enquiry',
    line='Exhausts, intakes and the parts that back up a remap.',
    lead='Exhausts, intakes and the supporting parts that let a remap actually work harder, all kept road legal.',
    price_note='Parts and fitting quoted per car.',
    options=[('Exhausts', 'Cat-back systems and tips, within noise limits.'), ('Intakes', 'Better breathing for Stage 2.'), ('Bolt-on modules', 'RaceChip and similar plug-ins.'), ('Quick shifters', 'For bikes.')],
    steps=[('Tell us the goal', 'Sound, power or both.'), ('Parts sourced', 'Matched to the car and the map.'), ('Fitted and checked', 'Leaks, fit and sound tested.')],
    good='Decats, DPF removal and sports cats without 103R approval aren\'t road legal and fail the MOT. We fit legal parts for road cars.',
    faq=[('Do I need a remap with an exhaust?', 'Not always; for Stage 2 gains, yes.'), ('Will it be too loud?', 'We keep road cars within legal noise limits.')],
    related=['remapping', 'air-suspension', 'coilovers'], blog=[('The legal reality of car mods in the UK', '#')])

# ---------------- STYLING ----------------
svc('car-wrapping', group='styling', name='Car wrapping', short='Car wrapping', chip='wrap',
    title='Car Wrapping in London: Full & Partial Wraps | Hyped Up',
    desc='Car wraps in Bermondsey, South London, from £1,500: full colour changes, roofs, stripes and chameleon, plus panels from £90. A full wrap takes at least a week.',
    img='abarth-pink-wrap.jpg', alt='Abarth 595 wrapped pink with gold wheels', price='from £1,500',
    line='Full colour changes, roofs, stripes, chameleon.',
    lead='A new colour without a respray. Full wraps, roofs, stripes and chameleon, with every panel prepped and every edge tucked. The prep is the job.',
    price_note='Full wraps from £1,500 for a compact car, more for bigger cars and supercars · panels from £90 · roofs from £200. A full wrap takes at least a week.',
    options=[('Full colour change', 'Gloss, satin, matte, chameleon.'), ('Partial wraps', 'Roof, bonnet, mirrors, race stripes.'), ('Door shuts', 'For a finish that looks like paint.'), ('Motorbike wraps', 'From £900.')],
    steps=[('Pick the colour', 'We\'ll show you samples and finishes.'), ('Drop the car off', 'A full wrap takes at least a week.'), ('Collect', 'Checked panel by panel with you.')],
    faq=[('How much does a car wrap cost?', 'From £1,500 for a full wrap on a compact car; bigger cars cost more. Send us the car and the colour.'), ('How long does a wrap take?', 'A full wrap takes at least a week.'),
         ('Does a wrap damage paint?', 'Not on healthy factory paint, fitted and removed properly.'), ('How long does a wrap last?', 'Several years with care. <span class="tbc">(TBC: Hypa)</span>')],
    related=['paint-protection-film', 'chrome-delete', 'window-tinting'], blog=[('How much does a car wrap cost in the UK?', '#')])

svc('paint-protection-film', group='styling', name='Paint protection film', short='Paint protection film', chip='wrap',
    title='Paint Protection Film (PPF) in London | Hyped Up',
    desc='Paint protection film fitted in Bermondsey, South London: clear or tinted PPF against stone chips and scratches, on the front end or the whole car.',
    img=None, need='a PPF job', alt='', price='price on enquiry',
    line='Clear film that takes the stone chips instead of your paint.',
    lead='A clear, tough film over the paint that takes the stone chips and scratches instead of your car. Gloss, satin or tinted.',
    price_note='Priced per car and coverage. <span class="tbc">(PPF prices TBC: Hypa)</span>',
    options=[('Front end', 'Bonnet, bumper, wings and mirrors: where chips happen.'), ('Full car', 'Every painted panel.'), ('Tinted PPF', 'Protection and a colour change in one.'), ('Satin PPF', 'Turns gloss paint satin.')],
    steps=[('Choose coverage', 'Front end or full car.'), ('Prep and fit', 'Paint cleaned and corrected first.'), ('Cure and collect', 'Checked with you.')],
    faq=[('PPF or ceramic coating?', 'PPF stops chips and scratches; ceramic makes paint easier to clean. Many people do both.'), ('Can PPF change the colour?', 'Tinted PPF can.')],
    related=['detailing', 'car-wrapping', 'window-tinting'], blog=[('Wrapping, PPF and window tints', '#')])

svc('window-tinting', group='styling', name='Window tinting', short='Window tinting', chip='wrap',
    title='Window Tinting in London: Legal Car Tints | Hyped Up',
    desc='Window tinting in Bermondsey, South London, from £150: dyed, carbon or ceramic film, with front windows kept within UK law.',
    img=None, need='a tint job', alt='', price='from £150',
    line='Dyed, carbon or ceramic film, fronts kept legal.',
    lead="Privacy, less heat and less glare, with carbon or ceramic film that won't turn purple. Rear windows any shade; fronts kept legal.",
    price_note='Rear windows from £150 · full car from £180 · sunstrip £45.',
    options=[('Dyed', 'Good-looking privacy at the lowest price.'), ('Carbon', 'Won\'t fade, cuts more heat.'), ('Ceramic', 'Best heat and glare rejection.'), ('Sunstrip', 'Top of the windscreen.')],
    steps=[('Pick the shade', 'We show you samples on the car.'), ('Fitted dust-free', ''), ('Leave it to cure', 'Windows up for a few days.')],
    good='UK law: the windscreen must let through at least 75% of light and the front side windows at least 70%. Rear windows can be any shade.',
    faq=[('Is window tint legal in the UK?', 'Rear windows, any shade. Windscreen 75% and front side windows 70% light minimum.'), ('How long does tinting take?', 'It depends on the car and the windows; we\'ll tell you when we quote.'),
         ('Can you tint headlights?', 'Ask us first: light tints can make a car illegal on the road. <span class="tbc">(Policy TBC: Hypa)</span>')],
    related=['paint-protection-film', 'car-wrapping', 'chrome-delete'], blog=[])

svc('air-suspension', group='styling', name='Air suspension', short='Air suspension', chip='air',
    title='Air Suspension Installation in London | Hyped Up',
    desc='Air suspension fitted in Bermondsey, South London, from £1,895: Air Lift Performance and Prazis, set up for daily driving and shows. Authorised dealer.',
    img='mini-jcw-low.jpg', alt='Red Mini JCW sitting low on air suspension', price='from £1,895',
    line='Air Lift and Prazis, set up for daily driving.',
    lead='Slammed when you park, up for speed bumps when you drive. Air Lift and Prazis, with the tank and compressor placed so you never hear them. Hypa runs his own Mini on Air Lift 3P every day.',
    price_note='From £1,895 for a classic boot install with a four-wheel alignment; full kits supplied and fitted quoted per car.',
    options=[('Air Lift Performance 3P / 3H', 'Presets on your phone, height sensors on 3H.'), ('Prazis', 'Quality kits for many cars.'), ('Boot builds', 'Tanks and compressors shown off or hidden.')],
    steps=[('Pick the kit', 'Matched to the car and how you drive.'), ('Fitted and aligned', 'Four-wheel alignment included.'), ('Set up with you', 'Presets and how to use it day to day.')],
    good='Tell your insurer about air suspension. <span class="tbc">(Authorised dealer wording TBC: Hypa)</span>',
    faq=[('Can you daily drive on air?', 'Yes. Hypa has daily driven his own Mini on air for over 4 years.'), ('Air or coilovers?', 'Air adjusts at the touch of a button; coilovers are fixed but simpler. See coilovers.'),
         ('How long does fitting take?', 'Usually 2–3 days. <span class="tbc">(TBC)</span>')],
    related=['coilovers', 'wheel-refurb', 'bodykits'], blog=[('The low life chose me: why air suspension changed everything', '#')])

svc('coilovers', group='styling', name='Coilovers & lowering springs', short='Coilovers & lowering', chip='air',
    title='Coilovers & Lowering Springs Fitted in London | Hyped Up',
    desc='Coilovers and lowering springs fitted in Bermondsey, South London, with alignment: a lower stance and sharper handling without going to air.',
    img=None, need='a coilover install', alt='', price='price on enquiry',
    line='A lower stance without going to air.',
    lead='Sharper handling and a lower stance at a fixed height. Coilovers if you want to adjust, springs for a simple drop, and an alignment after, every time.',
    price_note='Parts and fitting quoted per car, alignment included. <span class="tbc">(TBC: Hypa)</span>',
    options=[('Coilovers', 'Adjustable height and damping.'), ('Lowering springs', 'A simple, cheaper drop.')],
    steps=[('Pick the drop', 'How low, and how you drive.'), ('Fitted', 'With alignment.'), ('Checked', 'Ride height and handling on the road.')],
    faq=[('Coilovers or air?', 'Coilovers suit drivers who want a fixed, sporty setup; air suits those who want low at shows and practical day to day.')],
    related=['air-suspension', 'wheel-refurb', 'bodykits'], blog=[('Air suspension and bodykit fitting', '#')])

svc('chrome-delete', group='styling', name='Chrome delete', short='Chrome delete', chip='wrap',
    title='Chrome Delete in London: Trims & Badges | Hyped Up',
    desc='Chrome delete in Bermondsey, South London, from £50: window trims, grilles, badges and antennas wrapped gloss or satin black, fully reversible.',
    img=None, need='a chrome delete', alt='', price='from £50',
    line='Trims, grilles and badges blacked out.',
    lead='Chrome out, gloss or satin black in: window trims, grilles, badges. Fully reversible.',
    price_note='Antenna from £50 · window trims from £160.',
    options=[('Window trims', 'The biggest change for the money.'), ('Grilles and badges', 'Front and rear.')],
    steps=[('Pick the finish', 'Gloss or satin black.'), ('Wrapped', ''), ('Collect', '')],
    faq=[('Is a chrome delete reversible?', 'Yes, the wrap peels off.')],
    related=['car-wrapping', 'window-tinting', 'bodykits'], blog=[])

svc('bodykits', group='styling', name='Bodykits & exterior parts', short='Bodykits', chip='wrap',
    title='Bodykit Fitting in London: Spoilers, Splitters | Hyped Up',
    desc='Bodykits and exterior parts fitted in Bermondsey, South London, from £85: spoilers, splitters, skirts, diffusers and wide arch kits.',
    img=None, need='a bodykit fitting', alt='', price='from £85',
    line='Spoilers, splitters, skirts, wide arches.',
    lead='Spoilers, splitters, skirts, diffusers and wide arches, fitted straight with the gaps right. Bring your parts or we source them.',
    price_note='Rear spoiler from £85 · splitter from £145 · wide arch kit from £485.',
    options=[('Spoilers and splitters', ''), ('Side skirts and diffusers', ''), ('Wide arch kits', '')],
    steps=[('Send us the parts list', 'Or ask us to source them.'), ('Test fit', 'Before anything is fixed.'), ('Fitted', '')],
    faq=[('Can you fit parts I bought online?', 'Yes.')],
    related=['wheel-refurb', 'car-wrapping', 'air-suspension'], blog=[('Air suspension and bodykit fitting', '#')])

svc('wheel-refurb', group='styling', name='Wheel refurb & calipers', short='Wheel refurb & calipers', chip='wrap',
    title='Alloy Wheel Refurb & Caliper Painting London | Hyped Up',
    desc='Alloy wheel refurbishment and caliper painting in Bermondsey, South London, from £120 a wheel: kerb damage repaired, new colours, painted calipers.',
    img='volvo-gold-wheel.jpg', alt='Alloy wheel with a gold accent on a Volvo', price='from £120',
    line='Kerbed wheels fixed, new colours, painted calipers.',
    lead='Kerb rash repaired, wheels refinished in any colour and calipers painted to match.',
    price_note='From £120 a wheel · sets from £360 · caliper painting from £480.',
    options=[('Refurb', 'Kerb damage and corrosion repaired.'), ('Colour change', 'Any colour.'), ('Caliper painting', 'Any colour, heat-resistant.')],
    steps=[('Send photos', 'Of the damage.'), ('Refurbished', ''), ('Fitted and balanced', '')],
    faq=[('How long does a wheel refurb take?', '<span class="tbc">TBC: Hypa</span>')],
    related=['bodykits', 'air-suspension', 'detailing'], blog=[])

svc('interiors', group='styling', name='Interiors', short='Interiors', chip='other',
    title='Car Interior Upgrades in London: Carbon, Alcantara | Hyped Up',
    desc='Car interior upgrades in Bermondsey, South London: carbon trims, Alcantara, steering wheels and seats. Tell us the idea and we\'ll quote it.',
    img=None, need='an interior job', alt='', price='price on enquiry',
    line='Carbon trims, Alcantara, steering wheels, seats.',
    lead='Make the inside match the outside: carbon trims, Alcantara, steering wheels and seats.',
    price_note='Quoted per car and idea.',
    options=[('Carbon trims', ''), ('Alcantara', ''), ('Steering wheels', ''), ('Seats', '')],
    steps=[('Send the idea', 'Photos help.'), ('Quote', ''), ('Fitted', '')],
    faq=[], related=['ambient-lighting', 'car-audio', 'car-wrapping'], blog=[])

svc('detailing', group='styling', name='Detailing & ceramic coating', short='Detailing & ceramic', chip='wrap',
    title='Ceramic Coating & Paint Correction in London | Hyped Up',
    desc='Ceramic coating and paint correction in Bermondsey, South London, from £250: swirls removed, gloss back and paint protected.',
    img=None, need='a detailing job', alt='', price='from £250',
    line='Paint correction and ceramic coating.',
    lead='Swirls out, gloss back, then a ceramic coat that keeps it that way.',
    price_note='Ceramic coating from £250 · paint correction from £550.',
    options=[('Paint correction', 'Three levels, from a refresh to a full correction.'), ('Ceramic coating', 'Easier cleaning and lasting gloss.')],
    steps=[('Inspect the paint', ''), ('Correct', ''), ('Coat', '')],
    faq=[('PPF or ceramic?', 'PPF stops chips; ceramic makes cleaning easier. They work together.')],
    related=['paint-protection-film', 'car-wrapping', 'wheel-refurb'], blog=[('Car detailing, paint correction and ceramic coating', '#')])

svc('number-plates', group='styling', name='Number plates', short='Number plates', chip='plates',
    title='Same-Day Number Plates in London: 3D & 4D | Hyped Up',
    desc='Number plates made while you wait in Bermondsey, South London, from £30: standard, 3D gel, 4D laser-cut, show and magnetic plates.',
    img='porsche.jpg', alt='Porsche 911 outside the unit with a Hyped Up show plate', price='from £30',
    line='Standard, 3D gel, 4D, show plates. Made while you wait.',
    lead="Plates made while you wait: standard, 3D gel, 4D laser-cut, show and magnetic. Show plates are for shows, not the road, and we'll always tell you which is which.",
    price_note='From £30. <span class="tbc">(TBC: Hypa; live site says £35)</span>',
    options=[('Standard', ''), ('3D gel', ''), ('4D laser-cut', ''), ('Show plates', 'For shows only, not the road.')],
    steps=[('Bring your documents', 'V5C and ID, as the law requires.'), ('Made while you wait', ''), ('Fitted', '')],
    good='Road plates must meet the British Standard and you\'ll need your V5C and ID. Show plates aren\'t for the road. <span class="tbc">(Wording TBC: Hypa)</span>',
    faq=[('Are 4D plates legal?', 'Yes, when they meet the current British Standard. <span class="tbc">(TBC)</span>'), ('What do I need to bring?', 'Your V5C and photo ID.')],
    related=['chrome-delete', 'window-tinting'], blog=[('Custom number plates in London: same-day service', '#'), ('Number plate cloning is surging', '#')])

svc('van-signage', group='styling', name='Van signage & livery', short='Van signage & livery', chip='wrap',
    title='Van Signage & Livery in London | Hyped Up',
    desc='Van signage, livery and part wraps in Bermondsey, South London: your logo, phone number and colours on the road, designed and fitted.',
    img='ford-transit-yellow.jpg', alt='Yellow Ford Transit Custom in the workshop', price='price on enquiry',
    line='Logos, lettering and part wraps for vans.',
    lead='Turn the van into an advert: logos, lettering and part wraps, cut and fitted to last.',
    price_note='Quoted per van and design.',
    options=[('Lettering and logos', ''), ('Part wraps', ''), ('Full livery', '')],
    steps=[('Send your logo', ''), ('Design proof', ''), ('Fitted', '')],
    faq=[], related=['car-wrapping', 'reverse-cameras', 'car-trackers'], blog=[])

HUBS = {
    'security': dict(title='Car Security in South London: Ghost, Trackers | Hyped Up', h1='Car security',
        desc='Car and motorbike security fitted in Bermondsey, South London: Ghost immobilisers, trackers, alarms, dash cams and TfL taxi cameras. Clear "from" prices.',
        lead='Keyless cars and bikes get taken in South London every week, with relay kits, cloned keys and OBD hacks. We fit the security that stops them, finds them and puts it all on record.',
        img='porsche-macan-unit.jpg', alt='Porsche Macan outside the Hyped Up unit',
        layers=[('Stop it', 'Immobiliser'), ('Warn them', 'Alarm'), ('Find it', 'Tracker'), ('Prove it', 'Dash cam')],
        compare=[('Ghost immobiliser', 'Engine won\'t start without your PIN', 'Keyless cars, cloned keys', 'from £400'), ('Tracker', 'Live location, 24/7 monitoring', 'Getting it back', 'from £395'),
                 ('Alarm', 'Siren and phone alert', 'Street parking, break-ins', 'on enquiry'), ('Dash cam', 'Records driving and parked events', 'Crashes, claims, damage', 'from £125')],
        explainer=('S5 or S7 tracker?', 'Both track live with 24/7 monitoring and battery backup. S5 adds a driver tag, so an alert goes out the moment the car moves without you.'),
        faq=[('What security does a keyless car need?', 'An immobiliser first, because relay kits beat the factory key. Add a tracker for high-value cars.'),
             ('Do you fit security to motorbikes?', 'Yes: Ghost, trackers and alarms built for bikes.')]),
    'upgrades': dict(title='Car Upgrades in London: CarPlay, Audio, Remaps | Hyped Up', h1='Car upgrades',
        desc='Car upgrades in Bermondsey, South London: CarPlay, car audio, remapping, reverse cameras, ambient lighting and performance parts. Clear "from" prices.',
        lead='Make the car you have better to drive and live with: CarPlay, sound, power, cameras and lighting.',
        img='audi-r8-carplay.jpg', alt='Audi R8 dashboard with a new CarPlay screen',
        compare=[('CarPlay', 'Maps, music, calls on the dash', 'Older screens', 'from £170'), ('Car audio', 'Clearer sound, real bass', 'Flat factory systems', 'from £125'),
                 ('Remapping', 'More power and response', 'Healthy cars', 'from £250'), ('Reverse camera', 'See behind you', 'Tight parking, vans', 'from £125')],
        explainer=('Will CarPlay work in my car?', 'Most cars from about 2008 can have it, on a new screen or through an interface on the factory one. Send us the make, model and year.'),
        faq=[('Can you do several upgrades at once?', 'Yes, and it often saves labour: tell us everything you want.')]),
    'styling': dict(title='Car Styling in London: Wraps, PPF, Air | Hyped Up', h1='Car styling',
        desc='Car styling in Bermondsey, South London: wraps, PPF, tint, air suspension, coilovers, chrome delete, bodykits, wheels, interiors, detailing, plates and van signage.',
        lead='Make it look like nobody else\'s: colour, stance, wheels, details. Inside and out, cars, vans and bikes.',
        img='abarth-pink-wrap.jpg', alt='Abarth 595 wrapped pink with gold wheels',
        compare=[('Wrap', 'New colour, reversible', 'Colour change', 'from £1,500'), ('PPF', 'Stops chips and scratches', 'New or high-value paint', 'on enquiry'),
                 ('Ceramic', 'Gloss, easy cleaning', 'Every car', 'from £250'), ('Air suspension', 'Low on demand', 'Show and daily', 'from £1,895')],
        explainer=('Wrap, PPF or ceramic?', 'A wrap changes the colour. PPF protects the paint from chips. Ceramic makes it shine and easy to clean. Many cars get two of the three.'),
        faq=[('How long does a full wrap take?', 'At least a week.')]),
}

TBC = ['Ghost price (pricing.md £400; not in the sheet)', 'Alarm prices and alarm-repair offer', 'PPF, coilover, interior, signage prices', 'Remap prices (sheet has none; live site £435 / mobile £199)',
       'Which CarPlay price table is current', 'Number plates £30 vs £35', 'Insurer / Thatcham wording', 'Authorised dealer wording (Air Lift, Prazis)', 'OBD port protection: offered?',
       'Catalytic converter protection: offered? (251 searches/mo)', 'Light-tint and lighting legality wording', 'Fitting times for starlights, air, wheels', 'Builds captions']

# Meta descriptions, 155–160 characters each (checked by script); used by build.py over the inline ones.
DESCS = {
 'air-suspension': 'Air suspension fitted in Bermondsey, South London, from £1,895: Air Lift Performance and Prazis, set up for daily driving and shows, with alignment included.',
 'ambient-lighting': 'Ambient interior lighting, starlight headliners, door shadow lights and under-car lighting fitted in Bermondsey, South London, from £160, set from your phone.',
 'blog': 'Straight answers from Hypa\'s Bermondsey workshop: Ghost immobilisers, trackers, dash cams, CarPlay, remaps, wraps, air suspension and the UK law on car mods.',
 'bodykits': 'Bodykits and exterior parts fitted in Bermondsey, South London, from £85: spoilers, splitters, side skirts, diffusers and wide arch kits, test-fitted first.',
 'builds': 'Real cars and bikes from the Hyped Up workshop in Bermondsey: wraps, air suspension, CarPlay, audio, lighting and security installs. See the work, then ask.',
 'business': 'For London businesses, taxis and fleets: trackers, TfL-approved taxi cameras, van reverse cameras and sensors, and van signage, fitted in Bermondsey, SE16.',
 'car-alarms': 'Car alarms fitted and fixed in Bermondsey, South London: Scorpion alarms with tilt, shock and glass-break sensors and phone alerts. Alarm keeps going off? Ask.',
 'car-trackers': 'GPS car trackers fitted in Bermondsey, South London, from £395: S7 and S5 trackers with 24/7 monitoring and battery backup, plus trackers made for motorbikes.',
 'chrome-delete': 'Chrome delete in Bermondsey, South London, from £50: window trims, grilles, badges and antennas wrapped in gloss or satin black. Fully reversible, your way.',
 'coilovers': 'Coilovers and lowering springs fitted in Bermondsey, South London, with a full alignment: a lower stance and sharper handling for your car without going to air.',
 'detailing': 'Ceramic coating and paint correction in Bermondsey, South London, from £250: swirls and scratches removed, the deep gloss brought back and the paint sealed.',
 'ghost-immobiliser': 'Ghost immobiliser fitted in Bermondsey, South London, from £400. A PIN on your car\'s own buttons stops relay theft and cloned keys. For cars and motorbikes.',
 'home-a': 'Ghost immobilisers, trackers, CarPlay, car audio, remaps, wraps, PPF, tint and air suspension, fitted properly in Bermondsey, South London, with clear prices.',
 'home-b': 'Ghost immobilisers, trackers, CarPlay, car audio, remaps, wraps, PPF, tint and air suspension, fitted properly in Bermondsey, South London, with clear prices.',
 'interiors': 'Car interior upgrades in Bermondsey, South London: carbon trims, Alcantara, steering wheels and seats. Send your idea and photos and we\'ll quote it for you.',
 'motorbikes': 'Motorbike security, trackers, wraps and remaps in Bermondsey, South London: Ghost for bikes, Datatool S5 trackers, bike alarms, and motorbike wraps from £900.',
 'number-plates': 'Number plates made while you wait in Bermondsey, South London, from £30: standard, 3D gel, 4D laser-cut, show and magnetic plates. Bring your V5C and photo ID.',
 'paint-protection-film': 'Paint protection film fitted in Bermondsey, South London: clear, satin or tinted PPF against stone chips and scratches, on the front end or on the whole car.',
 'performance-parts': 'Exhausts, intakes and performance parts fitted in Bermondsey, South London, with a remap or on their own. Road-legal advice for cars and for motorbikes alike.',
 'remapping': 'ECU remapping in Bermondsey, South London: Stage 1, 2 and 3 for cars and motorbikes, done safely with KESS3 and JB4, plus honest advice on MOT and insurance.',
 'reverse-cameras': 'Reverse cameras and parking sensors fitted in Bermondsey, South London, from £125. For cars, vans and work vehicles, into your screen or onto a mirror monitor.',
 'security': 'Car and motorbike security fitted in Bermondsey, South London: Ghost immobilisers, GPS trackers, alarms, dash cams and TfL taxi cameras, with clear prices.',
 'styling': 'Car styling in Bermondsey, South London: wraps, PPF, tint, air suspension, coilovers, chrome delete, bodykits, wheels, interiors, detailing and number plates.',
 'taxi-cameras': 'TfL-approved camera systems fitted for London black cabs and private hire, from £395: 2SeeTV, HikVision and ACSS, installed and tested in Bermondsey, SE16.',
 'upgrades': 'Car upgrades in Bermondsey, South London: Apple CarPlay, car audio, ECU remapping, reverse cameras, ambient lighting and performance parts, with clear prices.',
 'van-signage': 'Van signage, livery and part wraps in Bermondsey, South London: your logo, phone number and colours on the road, designed with you, printed and fitted to last.',
 'wheel-refurb': 'Alloy wheel refurbishment and caliper painting in Bermondsey, South London, from £120 a wheel: kerb damage repaired, wheels in new colours, calipers painted.',
 'window-tinting': 'Window tinting in Bermondsey, South London, from £150: dyed, carbon or ceramic film for privacy and less heat, with the front side windows kept within UK law.',
}

# "How it works" (14 Nov, Dani): every job is bespoke. Step 1 = I listen; step 2 = a plan and price made for your car;
# step 3 = built to the plan and checked with you. Nothing is "while you wait" except number plates.
LISTEN = 'Tell us what you want'
STEPS = {
 'ghost-immobiliser': [(LISTEN, 'Your car, where it\'s parked and how you use it. We listen first.'), ('Your plan and price', 'Ghost, Metablok or Scorpion: we recommend what suits you, with a clear price.'), ('Fitted and checked with you', 'PIN set up together and the car tested before you drive away.')],
 'car-trackers': [(LISTEN, 'The car, what your insurer asks for, how you want alerts.'), ('Your plan and price', 'S7, S5 or bike tracker, plus the monthly cost, before you book.'), ('Fitted and checked with you', 'Hidden where a thief won\'t look; app set up with you.')],
 'dash-cams': [(LISTEN, 'How you drive, what you want recorded, any camera you already own.'), ('Your plan and price', '1, 2 or 3 cameras, parking mode, supplied or yours.'), ('Fitted and checked with you', 'Wiring hidden in the trims; app and footage shown to you.')],
 'car-alarms': [(LISTEN, 'A new alarm, or one that keeps going off? Tell us where you park.'), ('Your plan and price', 'The right sensors for your car and street.'), ('Fitted and checked with you', 'Sensitivity set and phone alerts tested together.')],
 'taxi-cameras': [(LISTEN, 'Your vehicle, licence type and working hours.'), ('Your plan and price', 'The approved system that fits your licence.'), ('Fitted and checked with you', 'Cameras, recorder and signage tested before you go back to work.')],
 'carplay': [(LISTEN, 'Your car, its year and how you use your phone in it.'), ('Your plan and price', 'New screen or factory screen, keeping your steering controls.'), ('Fitted and checked with you', 'Paired with your phone and shown working before you leave.')],
 'car-audio': [(LISTEN, 'What you listen to, how loud, and your budget.'), ('Your plan and price', 'Speakers, amps, subs or a full build, designed around your car.'), ('Built and tuned with you', 'Set up and played together until it sounds right.')],
 'remapping': [(LISTEN, 'Your car, how you drive it and what you want from it.'), ('Health check and plan', 'We read the ECU and check the car before anything is changed.'), ('Mapped and tested with you', 'Written for your car and checked on the road together.')],
 'reverse-cameras': [(LISTEN, 'Your car or van, its screen, where you struggle to park.'), ('Your plan and price', 'Camera, sensors or both, colour-matched.'), ('Fitted and checked with you', 'Guidelines and beeps set up with you.')],
 'ambient-lighting': [(LISTEN, 'The colours, the mood, the look you have in mind.'), ('Your design and price', 'Zones, colours and effects planned around your interior.'), ('Fitted and set up with you', 'No visible wires; controls shown on your phone.')],
 'performance-parts': [(LISTEN, 'Sound, power or both, and how road-legal it has to stay.'), ('Your plan and price', 'Parts matched to your car and your map.'), ('Fitted and checked with you', 'Fit, leaks and sound checked together.')],
 'car-wrapping': [(LISTEN, 'The colour, the finish, the look you want. Bring photos.'), ('Your design and price', 'Samples on your car, a clear price and a date. A full wrap takes at least a week.'), ('Checked with you, panel by panel', 'We go round the car together before you drive away.')],
 'paint-protection-film': [(LISTEN, 'How you use the car and how much you want covered.'), ('Your plan and price', 'Front end or full car, clear, satin or tinted.'), ('Fitted and checked with you', 'Paint prepared first, edges checked together.')],
 'window-tinting': [(LISTEN, 'How dark, how much heat you want to cut, which windows.'), ('Your shade and price', 'Samples on your car; fronts kept legal.'), ('Fitted and checked with you', 'Then windows up for a few days while it cures.')],
 'air-suspension': [(LISTEN, 'How low, how you drive day to day, shows or not.'), ('Your kit and price', 'Air Lift or Prazis, matched to your car and your life.'), ('Fitted and set up with you', 'Aligned, presets set, and shown how to live with it.')],
 'coilovers': [(LISTEN, 'How low and how you drive.'), ('Your plan and price', 'Coilovers or springs, with alignment.'), ('Fitted and checked with you', 'Ride height and handling checked on the road.')],
 'chrome-delete': [(LISTEN, 'Which chrome goes, and gloss or satin.'), ('Your plan and price', 'Trims, grilles, badges: as much or as little as you like.'), ('Wrapped and checked with you', 'Every edge checked together.')],
 'bodykits': [(LISTEN, 'The look, the parts you have or want.'), ('Your plan and price', 'Parts sourced or yours, test-fitted first.'), ('Fitted and checked with you', 'Straight, secure and checked together.')],
 'wheel-refurb': [(LISTEN, 'The damage, the colour, the finish you want.'), ('Your plan and price', 'Repair, colour and calipers planned together.'), ('Fitted and checked with you', 'Balanced, back on the car and inspected with you.')],
 'interiors': [(LISTEN, 'Your idea for the inside. Photos help.'), ('Your design and price', 'Materials and finishes chosen with you.'), ('Fitted and checked with you', 'Every detail checked before you drive away.')],
 'detailing': [(LISTEN, 'How the paint looks now and how you want it.'), ('Your plan and price', 'Correction level and coating chosen for your paint.'), ('Finished and checked with you', 'Inspected together in good light.')],
 'number-plates': [(LISTEN, 'Standard, 3D, 4D or show plates.'), ('Bring your documents', 'Your V5C and photo ID, as the law requires.'), ('Made while you wait', 'Plates are the one job we do on the spot.')],
 'van-signage': [(LISTEN, 'Your logo, your colours, what the van needs to say.'), ('Your design and price', 'A proof to approve before anything is printed.'), ('Fitted and checked with you', 'Checked together before it goes on the road.')],
}

# ---------- Google review on the homepage (rotates every 2–3 months) ----------
# Hypa/Dani pick one of the best real 5-star Google reviews and paste it here word for word with the reviewer's
# first name. The build shows the newest entry whose 'from' date has started. Add a new one every 2–3 months.
# Never write or edit a review: copy it exactly from Google.
GOOGLE_REVIEWS_URL = 'https://www.google.com/maps?cid=1418041190124790308'
GOOGLE_RATING = ('5.0', '47')  # Maps, 9 Nov 2026: update when it changes
REVIEWS = [
    {'from': '2026-11-01', 'name': 'Win Win', 'service': 'Bodykit fitting', 'source': 'Google, about 3 months before 18 Nov 2026',
     'full': "Last week I had my front splitter, front grille, side skirts, rear diffuser and rear spoiler installed at Hyped Up Ltd. The service here is extremely professional, with great attention paid to every tiny detail for vehicle modification. Every body panel fits seamlessly, all gaps are neatly aligned, and the final finish is flawless. No rushed work at all, and I was kept informed of every step during installation. I am thoroughly delighted with how my car looks after the job, and completely satisfied with the craftsmanship. I would highly recommend this shop for premium bodykit fitting.",
     'text': 'Every body panel fits seamlessly, all gaps are neatly aligned, and the final finish is flawless. No rushed work at all.'},
]

# ---------- v5 media (20 Nov 2026, Dani): Hypa in over half the media, about 50/50 video and photo ----------
# vid = silent square loop shown in the service hero; img = photo used for cards, picker backgrounds and proof.
# Clips and photos come from the Drive review (docs/design-build/drive-sort/video-review.md, media-log.md).
MEDIA_V5 = {
    'car-trackers': dict(vid='m1000rr-tracker.mp4', valt='BMW M1000RR in the workshop before a Scorpion tracker fit'),
    'dash-cams': dict(vid='dash-cam-mirror.mp4', valt='Mirror dash cam with live front and rear view, fitted in the workshop'),
    'carplay': dict(vid='carplay-screen-fitting-hypa.mp4', valt='Hypa fitting a new screen, the wiring loom on the bench, then wireless CarPlay working in a Mercedes',
                    img='carplay-saab-wiring-hypa.jpg', alt='Hypa wiring a double DIN CarPlay screen into a Saab 9-5'),
    'car-audio': dict(vid='boot-build-audio-hypa.mp4', valt='Hypa building a custom boot, sound deadening going on a door, a subwoofer grille close up',
                      img='e88-boot-speaker-pods-hypa.jpg', alt='Hypa wiring a BMW 1 Series boot with custom speaker pods in the boot lid'),
    'reverse-cameras': dict(vid='van-reverse-camera.mp4', valt='Brake-light reverse camera fitted on a van roof',
                            img='bmw-e88-screen.jpg', alt='New screen showing the reverse camera in a BMW 1 Series'),
    'ambient-lighting': dict(vid='starlight-headliner.mp4', valt='Hypa and the team threading starlight fibres, then the finished starlight headliner in an Alfa Romeo Stelvio'),
    'car-wrapping': dict(vid='evoque-satin-wrap.mp4', valt='Range Rover Evoque being wrapped in satin chameleon film inside the workshop',
                         img='subaru-camo-fitting-hypa.jpg', alt='Camo graphics going onto a Subaru Impreza, Hypa behind the car'),
    'paint-protection-film': dict(vid='ppf-headlights.mp4', valt='Mercedes X-Class headlight with protection film, outside the unit',
                                  img='ppf-headlights.jpg', alt='Mercedes X-Class headlight protected with clear film'),
    'window-tinting': dict(vid='window-tint-hypa-fitting.mp4', valt='Hypa tinting the rear windows of a white Corsa, then a black hatchback',
                           img='rear-tint-hypa-mural.jpg', alt='Hypa fitting rear window tint under the workshop mural'),
    'air-suspension': dict(vid='audi-s4-air-struts-hypa.mp4', valt='Hypa fitting air struts to a grey Audi S4 on the workshop floor',
                           img='s4-air-struts-hypa.jpg', alt='Black Audi on a Hyped Up show plate with new air struts boxed in front, Hypa at the bonnet'),
    'bodykits': dict(vid='lexus-splitter-fitting.mp4', valt='Front splitter being fitted to a Lexus in the workshop',
                     img='e88-grilles-hypa.jpg', alt='Hypa fitting gloss black kidney grilles to a BMW 1 Series'),
    'wheel-refurb': dict(vid='volvo-wheel-detail.mp4', valt='Volvo XC90 wheel with a yellow pinstripe on the rim'),
    'interiors': dict(img='a4-roof-deadening-hypa.jpg', alt='Hypa lying inside an Audi A4 Avant, sound deadening the roof'),
    'detailing': dict(img='bike-snow-foam-unit-22.jpg', alt='Hypa snow-foaming two motorbikes outside Unit 22'),
    'number-plates': dict(img='mt07-tail-tidy-hypa.jpg', alt='Hypa fitting a tail tidy and plate to a Yamaha MT-07, the plates price board behind'),
    'van-signage': dict(vid='van-lettering-hypa.mp4', valt='Hypa lettering a BDG Security van, the vinyl plotter cutting, a logo going on with the heat gun',
                        img='van-lettering-heat-gun-hypa.jpg', alt='Hypa setting van vinyl with a heat gun under the workshop mural'),
}
for _k, _v in MEDIA_V5.items(): S[_k].update(_v)
HUBS['security'].update(vid='dash-cam-mirror.mp4', valt='Mirror dash cam with live front and rear view')
HUBS['upgrades'].update(vid='carplay-screen-fitting-hypa.mp4', valt='Hypa fitting a new CarPlay screen')
HUBS['styling'].update(vid='evoque-satin-wrap.mp4', valt='Range Rover Evoque being wrapped in satin chameleon film')
# Files with Hypa in shot: counted by the build for the "Hypa in over half the media" rule.
HYPA_MEDIA = {'hyped-up-workshop-reel.mp4', 'window-tint-hypa-fitting.mp4', 'audi-s4-air-struts-hypa.mp4', 'carplay-screen-fitting-hypa.mp4',
              'boot-build-audio-hypa.mp4', 'starlight-headliner.mp4', 'van-lettering-hypa.mp4', 'hypa-in-the-workshop.mp4',
              'audi-a4-soundproofing-build.mp4', 'bmw-e88-build.mp4', 'bdg-van-livery.mp4', 'subaru-wrap-fitting.jpg', 'mini-opening-night.jpg',
              'bike-snow-foam-unit-22.jpg', 'bdg-van-fitting.jpg'}
# v5 tuning (media count: more video, more Hypa, without a second loop on any screen)
S['ghost-immobiliser'].update(vid='hypa-in-the-workshop.mp4', valt='Hypa in the driver seat of a customer car, then at the bench', img='hypa-in-the-workshop.jpg', alt='Hypa working in the driver seat of a customer car')
S['remapping'].update(vid='hypa-engine-bay.mp4', valt='Gloved hands in a BMW engine bay, then Hypa at the bench')
S['taxi-cameras'].update(vid='dash-cam-mirror.mp4', valt='Mirror dash cam with live front and rear view')
S['chrome-delete'].update(vid='e88-grille-black.mp4', valt='Gloss black kidney grilles on a BMW 1 Series', img='e88-grilles-hypa.jpg', alt='Hypa fitting gloss black kidney grilles to a BMW 1 Series')
S['coilovers'].update(img='s4-air-struts-hypa.jpg', alt='New struts boxed in front of a black Audi, Hypa at the bonnet')
S['interiors'].update(vid='starlight-headliner.mp4', valt='Starlight fibres being threaded, then the finished headliner lit up')
S['car-alarms'].update(vid='m1000rr-tracker.mp4', valt='BMW M1000RR in the workshop before a Scorpion alarm and tracker fit')
S['ambient-lighting'].update(img='starlight-headliner.jpg', alt='Hypa and the team threading starlight fibres into a headliner')
HYPA_MEDIA |= {'starlight-headliner.jpg', 'hypa-in-the-workshop.jpg'}
# "Recent work" leads with a build story loop (far below the hero, so still one moving piece per screen)
PROOF_REEL = {'car-audio': ('audi-a4-soundproofing-build.mp4', 'Audi A4 Avant', 'Deadening, air and audio', 'Hypa deadening an Audi A4, a boot trim refitted'),
              'carplay': ('audi-r8-carplay-reel.mp4', 'Audi R8', 'New CarPlay screen', 'Audi R8 CarPlay screen, then the car outside the unit'),
              'car-wrapping': ('mini-stripes-reel.mp4', 'Mini (own)', 'Stripes', 'Red Mini with black bonnet stripes'),
              'air-suspension': ('audi-a4-soundproofing-build.mp4', 'Audi A4 Avant', 'Air ride and a quiet cabin', 'Hypa working on an Audi A4 Avant'),
              'van-signage': ('bdg-van-livery.mp4', 'BDG Security van', 'Livery', 'Hypa fitting BDG Security lettering to a van'),
              'bodykits': ('bmw-e88-build.mp4', 'BMW 1 Series (own)', 'Fibreglass boot, new screen', 'Hypa building the BMW 1 Series'),
              'reverse-cameras': ('bmw-e88-build.mp4', 'BMW 1 Series (own)', 'Screen and reverse camera', 'Hypa building the BMW 1 Series'),
              'ambient-lighting': ('alfa-headliner.jpg', 'Alfa Romeo Stelvio', 'Black headliner', 'Alfa Romeo Stelvio black headliner')}
# v5.1 (20 Nov, Dani): service images show the finished product, crisp and close (no work-in-progress).
# Hypa-at-work stays in the hero loops, About, Builds and Community. Hypa share is not forced on service cards.
_FINISHED = {
    'ghost-immobiliser': ('alfa-keys-wheel.jpg', 'Alfa Romeo steering wheel, start button and keys with a MetaTrak tag'),
    'carplay': ('audi-r8-carplay.jpg', 'Audi R8 dashboard with a new screen showing the map and apps'),
    'car-audio': ('boot-build.jpg', 'Finished custom boot with a red and black subwoofer enclosure'),
    'car-wrapping': ('subaru-camo-wrap.jpg', 'Subaru with finished grey camo graphics under the workshop mural'),
    'window-tinting': ('tint-corsa-finished.jpg', 'White Vauxhall Corsa with finished rear window tint on a Hyped Up show plate'),
    'air-suspension': ('mini-jcw-low.jpg', 'Red Mini JCW sitting low on air suspension'),
    'ambient-lighting': ('bmw-ambient-blue.jpg', 'BMW interior lit with blue ambient lighting'),
    'interiors': ('alfa-headliner.jpg', 'Alfa Romeo Stelvio with a finished black headliner'),
    'bodykits': ('e88-grille-black.jpg', 'Gloss black kidney grilles fitted to a BMW 1 Series'),
    'chrome-delete': ('e88-grille-black.jpg', 'Gloss black kidney grilles fitted to a BMW 1 Series'),
    'number-plates': ('porsche.jpg', 'Porsche 911 outside the unit with a Hyped Up show plate'),
    'van-signage': ('bdg-van-beacons.jpg', 'BDG Security van with finished livery and a roof beacon bar'),
}
for _k, (_i, _a) in _FINISHED.items(): S[_k].update(img=_i, alt=_a)

# ---------- Focal points (20 Nov, Dani): crops always centre on the subject ----------
# CSS object-position "x% y%" per image; frames crop with object-fit:cover. Default for anything not listed: 50% 45%.
FOCUS = {
    'metatrak-mercedes-e-class-leaflet.jpg': '50% 54%', 'metatrak-audi-s4-wheel.jpg': '50% 40%',
    'mini-jcw-low.jpg': '50% 33%', 'mini-jcw-street.jpg': '50% 46%', 'alfa-keys-wheel.jpg': '35% 55%', 'r8-pioneer-screen.jpg': '50% 40%',
    'audi-r8-carplay.jpg': '50% 52%', 'subaru-camo-wrap.jpg': '50% 55%', 'porsche.jpg': '50% 62%', 'civic.jpg': '50% 52%', 'wrap.jpg': '50% 60%',
    'volvo-xc90-satin.jpg': '50% 55%', 'abarth-pink-wrap.jpg': '50% 62%', 'alfa-stelvio-pink.jpg': '50% 72%', 'bentley-unit.jpg': '50% 60%',
    'audi-r8-unit.jpg': '50% 60%', 'porsche-macan-unit.jpg': '50% 60%', 'tracker.jpg': '30% 62%', 'dashcam.jpg': '50% 28%',
    'merc-dashcam.jpg': '40% 65%', 'bmw-e88-screen.jpg': '65% 25%', 'mercedes-screen.jpg': '50% 22%', 'carplay.jpg': '50% 40%',
    'calipers-m.jpg': '50% 55%', 'tint-corsa-finished.jpg': '50% 62%', 'rear-tint-hypa-mural.jpg': '50% 60%', 's4-air-struts-hypa.jpg': '50% 58%',
    'carplay-saab-wiring-hypa.jpg': '35% 40%', 'e88-boot-speaker-pods-hypa.jpg': '45% 40%', 'subaru-camo-fitting-hypa.jpg': '45% 45%',
    'mt07-tail-tidy-hypa.jpg': '55% 55%', 'van-lettering-heat-gun-hypa.jpg': '40% 40%', 'hypa-carbon-streetfighter.jpg': '50% 55%',
    'bike-snow-foam-unit-22.jpg': '50% 58%', 'helmet.jpg': '50% 45%', 'r6-grass.jpg': '50% 55%', 'workshop.jpg': '50% 55%',
    'mini-opening-night.jpg': '50% 55%', 'remap.jpg': '50% 50%', 'boot-build.jpg': '50% 50%', 'abarth-ambient.jpg': '50% 50%',
    'bdg-van-beacons.jpg': '50% 50%', 'mini-jcw-show.jpg': '50% 50%', 'skyline-r34.jpg': '50% 50%', 'alfa-headliner.jpg': '50% 40%',
    'meet-entrance-hypa-ruff-ryders.jpg': '50% 55%', 'meet-unit-22-crowd.jpg': '50% 60%', 'meet-hayabusa-ruff-ryders.jpg': '50% 50%',
    'meet-mini-sub-boot.jpg': '50% 62%', 'mt07-red-mini.jpg': '50% 55%', 'giulia-tint-hypa.jpg': '50% 55%', 'cx5-tint-hypa.jpg': '50% 45%',
    'e88-grilles-hypa.jpg': '55% 45%', 'ford-transit-yellow.jpg': '50% 55%', 'workshop-floor.jpg': '50% 45%',
}
S['car-trackers'].update(img='metatrak-mercedes-e-class-leaflet.jpg', alt='MetaTrak leaflet, key and tracker tag held up in front of a black Mercedes E-Class on a Hyped Up plate')
# ---------- v5.3 (21 Nov, Dani): fewer repeats ----------
# A service's main image stays on its own page and its hub card (so you know where you are).
# "Related" rows rotate through other real examples from POOL, so the same service shows a different job on each page.
S['ghost-immobiliser'].update(img='ghost-start-button-wheel.jpg', alt='Alfa Romeo start button and stitched steering wheel')
S['chrome-delete'].update(img='e88-grilles-hypa.jpg', alt='Hypa fitting gloss black kidney grilles to a BMW 1 Series')
FOCUS.update({'ghost-start-button-wheel.jpg': '35% 25%', 'metatrak-audi-s4-wheel.jpg': '50% 62%', 'mercedes-screen.jpg': '50% 22%',
              'abarth-ambient-door.jpg': '50% 50%', 'bdg-van-rear.jpg': '50% 55%', 'minibus-signage.jpg': '50% 50%', 'lexus-splitter-fitting.jpg': '50% 50%'})
POOL = {
    'ghost-immobiliser': [('hypa-in-the-workshop.jpg', 'Hypa working in the driver seat of a customer car')],
    'car-trackers': [('metatrak-audi-s4-wheel.jpg', 'MetaTrak tag on the keys and the leaflet behind an Audi S4 steering wheel'), ('alfa-keys-wheel.jpg', 'MetaTrak tag on the keys of an Alfa Romeo'), ('m1000rr-tracker.jpg', 'BMW M1000RR in for a Scorpion tracker')],
    'dash-cams': [('merc-dashcam.jpg', 'Thinkware dash cam box in front of a white Mercedes E-Class'), ('dash-cam-mirror.jpg', 'Mirror dash cam with front and rear view')],
    'car-alarms': [('m1000rr-tracker.jpg', 'BMW M1000RR in the workshop')],
    'taxi-cameras': [('dash-cam-mirror.jpg', 'Mirror dash cam with front and rear view')],
    'carplay': [('mercedes-screen.jpg', 'Mercedes with a large new widescreen'), ('carplay.jpg', 'Mini with a new round CarPlay screen'), ('r8-pioneer-screen.jpg', 'Audi R8 Pioneer screen')],
    'car-audio': [('e88-boot-speaker-pods-hypa.jpg', 'Hypa wiring custom speaker pods in a BMW 1 Series boot'), ('meet-mini-sub-boot.jpg', 'Mini with a red custom subwoofer boot')],
    'remapping': [('hypa-engine-bay.jpg', 'Hands in a BMW engine bay')],
    'reverse-cameras': [('mercedes-screen.jpg', 'Mercedes widescreen showing the reverse camera guidelines'), ('van-reverse-camera.jpg', 'Brake-light reverse camera on a van roof')],
    'ambient-lighting': [('abarth-ambient.jpg', 'Abarth interior lit purple'), ('abarth-ambient-door.jpg', 'Abarth door open with ambient lighting')],
    'performance-parts': [('skyline-r34.jpg', 'Nissan Skyline R34 with the bonnet up')],
    'car-wrapping': [('alfa-stelvio-pink.jpg', 'Matte pink Alfa Romeo Stelvio with white wheels'), ('wrap.jpg', 'London taxi wrapped purple'), ('volvo-xc90-satin.jpg', 'Satin Volvo XC90 with gold wheel details')],
    'window-tinting': [('giulia-tint-hypa.jpg', 'Alfa Romeo Giulia being tinted'), ('rear-tint-hypa-mural.jpg', 'Hypa fitting rear tint under the mural')],
    'air-suspension': [('mini-jcw-street.jpg', 'Red Mini JCW low on air, on the street'), ('s4-air-struts-hypa.jpg', 'New air struts in front of a black Audi')],
    'bodykits': [('lexus-splitter-fitting.jpg', 'Front splitter going onto a Lexus')],
    'chrome-delete': [('e88-grille-black.jpg', 'Gloss black kidney grilles on a BMW 1 Series')],
    'wheel-refurb': [('calipers-m.jpg', 'Brake calipers painted red'), ('volvo-wheel-detail.jpg', 'Volvo wheel with a yellow pinstripe')],
    'interiors': [('a4-roof-deadening-hypa.jpg', 'Hypa deadening an Audi A4 roof'), ('starlight-headliner.jpg', 'Starlight fibres being threaded')],
    'number-plates': [('mt07-tail-tidy-hypa.jpg', 'Hypa fitting a plate to a Yamaha MT-07'), ('mini-jcw-show.jpg', 'Red Mini on a Hyped Up show plate')],
    'van-signage': [('bdg-van-rear.jpg', 'BDG Security van rear doors'), ('minibus-signage.jpg', 'Charity minibus lettering'), ('van-lettering-heat-gun-hypa.jpg', 'Hypa setting van vinyl with a heat gun')],
}
# ---------- v5.4 (21 Nov, Dani): more FAQs, deeper answers (hubs 5, every service at least 4) ----------
# Facts only from this file, memory/ and UK law. No new prices, no time promises except plates (while you wait) and wraps (1 week minimum).
HUBS['security']['faq'] = [
    ('What security does a keyless car need?', 'Keyless cars are the ones thieves target with relay kits: they boost the signal from your key inside the house and drive off in seconds. Start with an immobiliser such as Ghost, so the car won\'t start without your PIN even if the key signal is copied. Add a monitored tracker on anything high value, so if it does go, it can be found. A dash cam with parking mode and an alarm with phone alerts are the next layers.'),
    ('Ghost or a tracker: which should I fit first?', 'If you can only do one, fit the immobiliser: it stops the car being driven away. A tracker doesn\'t stop the theft, it helps get the car back, and many insurers ask for one on prestige cars. Most of our customers end up with both, because together they cover the two ways a car gets taken: driven off, or lifted onto a truck.'),
    ('Do you fit security to motorbikes?', 'Yes. A bike can be lifted into a van in under a minute, so an immobiliser alone isn\'t enough. We fit Ghost to bikes, compact S5 trackers hidden under the seat or in the tail, and alarms with motion and shock sensors. See Motorbikes for what we fit and the bikes we\'ve done.'),
    ('Do I need to tell my insurer?', 'Yes, tell them what you\'ve fitted. Some insurers ask for a specific tracker category or an approved immobiliser before they\'ll cover a car, and some take it into account in the price. We give you the paperwork after fitting, so you have the details to hand.'),
    ('How much does car security cost?', 'Ghost immobilisers start from £400, monitored trackers from £395 plus the monthly monitoring subscription, and dash cams from £125 fitted. The exact price depends on the car and what you want to protect against. Tell us the make, model and year and we\'ll come back with a straight price for the setup we\'d actually recommend.'),
]
HUBS['upgrades']['faq'] = [
    ('Can you do several upgrades at once?', 'Yes, and it usually makes sense. A screen, a reverse camera and new speakers all mean taking the same trim off, so doing them together saves labour and means the car is only apart once. Tell us everything you want and we\'ll plan it as one job, with one price.'),
    ('Will I keep my steering wheel controls and factory features?', 'Yes. With a new screen or a CarPlay interface we keep your steering wheel controls working, and with audio we can keep the factory head unit if you like the look. If a feature can\'t be kept on your car, we tell you before we start, not after.'),
    ('Can my car keep a factory look?', 'Often, yes. A CarPlay interface sits behind the original screen so the dash looks standard, amps and subs can be hidden in the boot floor, and ambient lighting is wired into the existing trim. If you want it loud and visible instead, we build that too.'),
    ('Does a remap affect my insurance or warranty?', 'A remap is a modification, so tell your insurer. We read the ECU and check the car is healthy before anything is changed, and map it for the hardware it actually has, so the engine isn\'t pushed past what it can take. If your car is still under a manufacturer warranty, ask them first.'),
    ('Do you supply the parts, or can I bring my own?', 'Both. We supply brands we trust, such as Pioneer, Kenwood, Xtrons, Autostyle and Rockford Fosgate. If you\'ve already bought a screen, camera or dash cam, we can fit it: we\'ll check it suits your car first.'),
]
HUBS['styling']['faq'] = [
    ('How long does a full wrap take?', 'At least a week. Panels, handles and lights come off, every surface is cleaned and prepped, and the film is laid and tucked edge by edge. Rushing the prep is what makes wraps lift and peel, so we don\'t. Smaller jobs like a roof, mirrors or chrome delete are quicker: we\'ll give you the timing when we quote.'),
    ('Can you wrap just part of the car?', 'Yes. Roofs, bonnets, mirrors and race stripes are popular, and chrome delete turns shiny trims black. It\'s a big change for less money and less time than a full wrap, and it comes off later if you want the original look back.'),
    ('Is window tint legal?', 'Rear side windows and the rear screen can go as dark as you like. UK law says the front side windows must let at least 70% of light through and the windscreen at least 75%, so we won\'t black out the fronts. We\'ll show you the shades that keep you legal.'),
    ('Will a wrap damage my paint?', 'On healthy factory paint, a good-quality film comes off cleanly when you want it removed. Resprayed panels, chips and peeling lacquer are a different story, so we check the paint before we start and tell you straight if there\'s a risk.'),
    ('How do I look after a wrap or PPF?', 'Hand wash, keep a pressure washer away from the edges, and avoid automatic brush washes. We go through the aftercare with you when you collect the car. A ceramic coating on top makes washing easier and helps the finish stay clean.'),
]
_MORE = {
    'car-alarms': [('Can an alarm alert my phone?', 'Yes. Modern Scorpion alarms send tamper alerts to an app, and you can arm and disarm from your phone. That matters more than the siren, because on a busy street a siren on its own gets ignored.')],
    'taxi-cameras': [('Why does my taxi need an approved camera?', 'TfL sets the rules for cameras in licensed taxis and private hire vehicles. Only approved systems meet them, so fitting a general dash cam inside the cab isn\'t the same thing. We\'ll confirm the right system for your licence before you book.'),
                     ('Can you fit a camera to a black cab and a PHV?', 'Yes, both. We fit approved 2-channel systems from 2SeeTV and HikVision, and ACSS as an alternative. Tell us the vehicle and the licence type and we\'ll match the system.')],
    'car-audio': [('Why deaden the doors before new speakers?', 'A door is a thin metal box that rattles and leaks sound. Deadening it first makes even a modest speaker sound tighter and louder, and cuts road noise too. It\'s the upgrade people notice most for the money.')],
    'reverse-cameras': [('Can a reverse camera go into my factory screen?', 'On many cars, yes, using an interface; on others it goes into a new screen. Tell us the car and year and we\'ll say which.'),
                        ('Do you fit cameras to vans?', 'Yes. Brake-light cameras and mirror monitors are the usual setup for vans, wired in neatly so they work every time you select reverse.')],
    'ambient-lighting': [('What\'s a starlight headliner?', 'Hundreds of fibre optic points threaded one by one through the roof lining, so with the lights off the roof looks like a night sky. It\'s detailed, slow work: see the Alfa Romeo Stelvio in Builds.'),
                         ('Can I change the colours?', 'With most ambient kits, yes: colours and brightness change from a phone app or the car\'s controls, depending on the kit.')],
    'performance-parts': [('Will an exhaust make my car fail its MOT?', 'It can if it\'s too loud or the emissions parts are removed. We\'ll tell you straight what\'s road legal on your car and what isn\'t before you buy anything.'),
                          ('Do I need a remap with new parts?', 'Sometimes. Intakes and exhausts on their own make a small difference; on many turbo cars a map is what unlocks the gain. We\'ll tell you what\'s worth doing on your car.')],
    'paint-protection-film': [('What does PPF protect against?', 'Stone chips, scratches, bird droppings and the small marks that build up on the front of a car. The film is clear, so the paint looks the same, just protected.'),
                              ('Front end only, or the whole car?', 'Most people start with the high-impact areas: bumper, bonnet, wings and mirrors. Full-car PPF is an option for new and high-value cars. We\'ll quote both so you can choose.')],
    'window-tinting': [('Can you tint the front windows?', 'Only within the law: the front side windows must let at least 70% of light through and the windscreen 75%. Rear windows can go darker. We\'ll show you shades that keep you legal.')],
    'air-suspension': [('Can I still drive over speed bumps?', 'Yes. That\'s the point of air: low when parked, raised at the press of a button for speed bumps, ramps and driveways. We set the system up and show you how it works before you leave.')],
    'coilovers': [('Coilovers or lowering springs?', 'Springs are the simpler, cheaper way to drop the car a fixed amount. Coilovers let you set the height, and on many kits the damping, so you can tune the stance and the ride.'),
                  ('Will lowering affect the ride?', 'A little, and that\'s the trade-off. A good kit set up properly rides well day to day. We\'ll help you pick a drop that suits the roads you drive.'),
                  ('Does it need a wheel alignment afterwards?', 'Yes, lowering changes the geometry, so the car needs an alignment after fitting. We\'ll explain this when we quote.')],
    'chrome-delete': [('What is a chrome delete?', 'The chrome trim around windows, grilles and badges is covered in gloss or satin black film, for a cleaner, darker look.'),
                      ('Is it permanent?', 'No. The film can be removed later and the original chrome is underneath, which makes it a good choice on leased or newer cars.'),
                      ('Can you do grilles and badges too?', 'Yes. Grilles can be wrapped or swapped for gloss black parts, like the kidney grilles on our own BMW 1 Series.')],
    'bodykits': [('Do you supply the parts?', 'We can source them, or fit parts you\'ve bought. We check the fit first, because cheap kits often need work to line up.'),
                 ('Can you fit splitters, spoilers and diffusers?', 'Yes, from a front splitter like the Lexus in Builds to full kits. We line them up properly so the gaps are even and nothing rattles.'),
                 ('Will parts need painting?', 'Some come finished in gloss black, some need painting to match. We\'ll tell you which when we quote.')],
    'wheel-refurb': [('What does a wheel refurb fix?', 'Kerb damage, scuffs and tired finishes. Wheels can go back to the original look or a new colour.'),
                     ('Can you paint the calipers?', 'Yes, calipers can be painted in a colour to match or contrast, like the red set in Builds.'),
                     ('What is AlloyGator?', 'A rim protector fitted between the tyre and the wheel edge, so kerbs hit the guard instead of the alloy. A good idea on new wheels.')],
    'interiors': [('What can you do inside a car?', 'Headliners, starlight roofs, ambient lighting, sound deadening and trim upgrades. Tell us the look and we\'ll say what\'s possible.'),
                  ('Can you redo my headliner?', 'Yes, from re-covering a sagging lining to a full starlight roof like the Alfa Romeo Stelvio in Builds.'),
                  ('Can you make my car quieter?', 'Yes. Sound deadening on the floor, doors and roof cuts road noise noticeably: see the Audi A4 in Builds.'),
                  ('Is my car off the road for long?', 'It depends on the job. We\'ll give you the timing with the quote.')],
    'detailing': [('What\'s ceramic coating?', 'A hard, glossy layer bonded to the paint that repels water and dirt, so the car stays cleaner and is easier to wash.'),
                  ('Can you coat a wrap or PPF?', 'Yes, coatings work on film as well as paint and make it easier to look after.'),
                  ('Do you detail motorbikes?', 'Yes. Bikes get a proper wash and detail too, before a ride out or after a long winter.')],
    'number-plates': [('Are your plates road legal?', 'Yes, road-legal plates need proof of identity and entitlement to the registration, and we\'ll tell you what to bring.'),
                      ('What are 3D and 4D plates?', '3D gel plates have raised, domed lettering; 4D plates have laser-cut raised letters for a sharper look.')],
    'van-signage': [('Do you design the signage too?', 'Bring your logo and we\'ll lay it out to suit the van, or tell us what you need and we\'ll help with the layout.'),
                    ('Do you cut the vinyl yourselves?', 'Yes, lettering and logos are cut on our own plotter in the unit, then fitted by hand.'),
                    ('Can you do a whole fleet?', 'Yes. Send us the vans and the design and we\'ll plan the fitting around your working day.'),
                    ('Can you fit beacons and lights?', 'Yes, like the roof beacon bar on the BDG Security van in Builds.')],
}
for _k, _v in _MORE.items(): S[_k]['faq'] = list(S[_k]['faq']) + _v

# ---------------- v5.5: "What we offer" (replaces "Pick your setup") ----------------
# Each option: (name, what it is, why choose it, who it's for). Facts only from memory/ and the copy above.
OFFER_INTRO = {
    'ghost-immobiliser': 'Four ways to stop your car starting without you. Each one does it differently.',
    'car-trackers': 'Three types of tracker. All of them are hidden, wired in and watched 24/7.',
    'dash-cams': 'Four set-ups, from one camera to full cover while you\'re parked.',
    'car-alarms': 'Alarms for cars and bikes, plus a fix for alarms that keep going off.',
    'taxi-cameras': 'Approved camera systems for black cabs and private hire, or we fit the one you bought.',
    'carplay': 'Three ways to get CarPlay and Android Auto, depending on the screen you have now.',
    'car-audio': 'Four upgrades. Start with one or build the full system in stages.',
    'remapping': 'Four levels of remap, from software only to full builds and bikes.',
    'reverse-cameras': 'Cameras and sensors, for front, rear and work vehicles.',
    'ambient-lighting': 'Four lighting upgrades, inside and out.',
    'performance-parts': 'Parts that add sound, response and power. They often go with a remap.',
    'car-wrapping': 'Full colour changes, smaller details and bikes.',
    'paint-protection-film': 'Clear film that takes the chips so your paint doesn\'t.',
    'window-tinting': 'Three tint films and a sunstrip. All of them are fitted inside the glass.',
    'air-suspension': 'Air kits from the brands we trust, plus the boot build to show it off.',
    'coilovers': 'Two ways to lower your car.',
    'chrome-delete': 'Shiny trim turned black, one area at a time or the whole car.',
    'bodykits': 'Exterior parts that change the car\'s shape.',
    'wheel-refurb': 'Wheels repaired, recoloured, and calipers to match.',
    'interiors': 'Inside upgrades you notice every time you get in.',
    'detailing': 'Paint brought back, then protected.',
    'number-plates': 'Road-legal plates in three styles, plus show plates.',
    'van-signage': 'From a logo on the door to a full wrap.',
}
OFFER = {
    'ghost-immobiliser': [
        ('Ghost II', 'A hidden immobiliser that needs a PIN entered on buttons your car already has: steering wheel, windows or doors.', 'No fob to clone, no signal to relay, no box or LED for a thief to find.', 'Keyless cars at risk of relay theft, and motorbikes.'),
        ('Metablok and Metablok-e', 'An immobiliser that works with a tag in your pocket instead of a PIN. The e version adds app control. From £495.', 'Nothing to remember: the car starts when the tag is with you.', 'Drivers who\'d rather not enter a PIN every time, or who share the car.'),
        ('Scorpion X-series', 'An immobiliser built to work with Scorpion trackers and alarms. From £495.', 'One system for blocking the start, tracking and the alarm.', 'Drivers who want full security from one brand.'),
        ('OBD port protection', 'A lock on the diagnostic port under the dash. <span class="tbc">(TBC: Hypa)</span>', 'Thieves plug into that port to code a new key. This stops them.', 'Cars targeted by key-programming theft, usually fitted alongside an immobiliser.')],
    'car-trackers': [
        ('S7 trackers', 'A GPS tracker (SmartTrack Trident) with a 24/7 monitoring centre and battery backup.', 'You get an alert if the car moves or the battery is cut, and the centre helps the police get it back.', 'Most cars, and drivers whose insurer asks for a monitored tracker.'),
        ('S5 trackers', 'Everything S7 does (MetaTrak, Scorpion), plus a driver tag you carry.', 'If the car moves without the tag, the alert goes out straight away, even with your key.', 'High-value cars and anyone worried about cloned keys.'),
        ('Motorbike trackers', 'A small Datatool S5 unit hidden under the seat or in the tail.', 'Bikes can be lifted into a van in seconds. This tells you where it went.', 'Riders who park on the street or leave the bike overnight.')],
    'dash-cams': [
        ('Front', 'One camera on the windscreen, recording the road ahead, wired in neatly.', 'Evidence of what happened in front of you, without wires hanging down.', 'Everyday drivers who want simple cover at the lowest price.'),
        ('Front and rear', 'A second camera on the back window, recording both ways at once.', 'Covers the most common claims: being hit from behind and cash-for-crash.', 'Commuters and anyone driving in London traffic.'),
        ('3-channel', 'Front, rear and a third camera filming inside the car.', 'A record of what happens in the cabin as well as on the road.', 'Taxi, private hire and delivery drivers.'),
        ('Parking mode', 'The camera wakes and records when the car is knocked while parked. Battery protection is included.', 'Catches bumps and break-ins when you\'re not there, without flattening the battery.', 'Drivers who park on the street or in shared car parks.')],
    'car-alarms': [
        ('Scorpion alarms', 'A car alarm with shock, tilt and glass-break sensors, armed and disarmed from your phone.', 'You get a tamper alert on your phone, not just a siren in the street.', 'Cars without a factory alarm, or with one that does too little.'),
        ('Motorbike alarms', 'A loud siren with motion and shock sensors, hidden on the bike.', 'Puts thieves off before the bike is moved or lifted.', 'Riders who park on the street, often paired with a tracker.'),
        ('Alarm repair', 'We find out why your alarm keeps going off and fix or replace it. <span class="tbc">(TBC: Hypa)</span>', 'It\'s usually a sensor set too sensitive or a weak battery. Neighbours stop complaining.', 'Anyone whose alarm goes off for no reason.')],
    'taxi-cameras': [
        ('2SeeTV and HikVision 2-channel', 'Approved two-camera systems for licensed vehicles.', 'Meets the licensing rules and protects you and your passengers.', 'Black cab and private hire (PHV) drivers.'),
        ('ACSS EC2', 'Another approved system, fitted the same careful way.', 'A second approved option if it suits your vehicle better.', 'Drivers comparing approved systems.'),
        ('Install only', 'You bring an approved system, we fit and test it.', 'You keep the kit you chose and get a tidy, working install.', 'Drivers who\'ve already bought their cameras.')],
    'carplay': [
        ('New screen', 'A screen made for your car (Xtrons or Autostyle), or a Pioneer or Kenwood double DIN.', 'A bigger, modern screen with CarPlay and Android Auto built in.', 'Older cars with a small screen, or no screen at all.'),
        ('Keep your factory screen', 'A CarPlay interface fitted behind the dash, working through the screen you already have.', 'Looks exactly like standard, and works wireless.', 'Drivers who like their dash as it is and just want the apps.'),
        ('Add a reverse camera', 'A rear camera wired straight into the new screen.', 'Easier parking, fitted in the same visit.', 'Anyone upgrading their screen.')],
    'car-audio': [
        ('Speakers', 'New speakers in the doors, fitted properly.', 'Clearer sound, and the cheapest big upgrade you can make.', 'Anyone whose factory sound is flat or muddy.'),
        ('Amps and subwoofers', 'Rockford Fosgate amplifiers and subs, wired and tuned.', 'Bass you can feel, without rattles.', 'Drivers who want real volume and depth.'),
        ('Sound deadening', 'Damping material in the doors, or across the whole floor.', 'A quieter cabin and tighter bass from the speakers you have.', 'Daily drivers and anyone adding a sub.'),
        ('Custom boot builds', 'Enclosures with Alcantara and LED, built for your boot.', 'A system that looks as good as it sounds.', 'Show cars and builds that get the boot open at meets.')],
    'remapping': [
        ('Stage 1', 'A software remap of the engine\'s settings, no new parts.', 'More power and a smoother pull from the car you already have.', 'Standard cars, and the best first step.'),
        ('Stage 2', 'A remap matched to supporting parts like an intake and exhaust.', 'Gets the most from those parts, safely.', 'Cars that already have, or are getting, upgraded parts.'),
        ('Stage 3', 'A remap for bigger hardware changes, quoted per build.', 'Tuned around the whole build, not a file off the shelf.', 'Serious builds with major parts fitted.'),
        ('Motorbike remaps', 'The same careful remapping, for bikes.', 'Better response and a smoother ride.', 'Riders who want more from their bike.')],
    'reverse-cameras': [
        ('Reverse camera', 'A rear camera shown on a CarPlay screen, your factory screen or a mirror monitor.', 'See what\'s behind you, not just hear it.', 'Anyone parking in tight streets, especially with bigger cars.'),
        ('Rear parking sensors', 'Colour-matched sensors in the rear bumper that beep as you get close.', 'Fewer scrapes, and they blend into the paint.', 'Cars without factory sensors.'),
        ('Front parking sensors', 'Sensors in the front bumper.', 'Stops nose-first knocks on bollards and walls.', 'Drivers parking in tight London spaces.'),
        ('Vans and work vehicles', 'Cameras and sensors for vans and fleets.', 'Safer reversing and fewer repair bills.', 'Trades, delivery drivers and fleet managers.')],
    'ambient-lighting': [
        ('Ambient lighting', 'Light strips in the dash and doors, colour set from your phone.', 'Changes the feel of the car every time you drive at night.', 'Anyone who wants a premium feel inside.'),
        ('Starlight headliner', 'Hundreds of fibre-optic stars set into the roof lining.', 'The look of a luxury car in your own.', 'Drivers who want the biggest wow inside.'),
        ('Door shadow lights', 'Lights under the doors that show your logo on the ground.', 'A detail people notice when you get out.', 'Owners who love the small touches.'),
        ('Under-car lighting', 'Lights under the car.', 'Makes the car stand out at shows.', 'Show cars.')],
    'performance-parts': [
        ('Exhausts', 'Cat-back systems and tips, within noise limits.', 'A better sound and look, and more flow.', 'Drivers who want the car to sound like it should.'),
        ('Intakes', 'Air intakes that help the engine breathe.', 'Part of a Stage 2 set-up.', 'Cars going beyond a Stage 1 remap.'),
        ('Bolt-on modules', 'Plug-in modules such as RaceChip.', 'More power without a full remap.', 'Drivers who want an easy, reversible gain.'),
        ('Quick shifters', 'Clutchless up-shifts for motorbikes.', 'Faster, smoother gear changes.', 'Riders who want sharper response.')],
    'car-wrapping': [
        ('Full colour change', 'The whole car wrapped in a new colour: gloss, satin, matte or chameleon. It takes at least a week.', 'A new look without a respray, and the paint underneath stays protected.', 'Owners who want a change but want to keep the original paint.'),
        ('Partial wraps', 'Roof, bonnet, mirrors or race stripes.', 'A big change for less money and less time.', 'Drivers who want contrast or a sporty touch.'),
        ('Door shuts', 'The edges inside the doors wrapped too.', 'Opens the door and still looks like paint.', 'Full colour changes that need to look factory.'),
        ('Motorbike wraps', 'Tank, fairings and panels wrapped. From £900.', 'A new colour and protection for the bodywork.', 'Riders who want their bike to stand out.')],
    'paint-protection-film': [
        ('Front end', 'Clear film on the bonnet, bumper, wings and mirrors.', 'That\'s where stone chips happen. The film takes them, not the paint.', 'New and newer cars, and anyone doing motorway miles.'),
        ('Full car', 'Every painted panel covered.', 'The whole car protected from chips and scratches.', 'High-value cars and owners keeping the car for years.'),
        ('Tinted PPF', 'Protection film with a colour.', 'A colour change and protection in one.', 'Owners who want a new shade and full protection.'),
        ('Satin PPF', 'Film that turns gloss paint satin.', 'A satin finish that also protects.', 'Drivers who like the satin look.')],
    'window-tinting': [
        ('Dyed', 'A dyed film for privacy at the lowest price.', 'Darker windows and a cleaner look for less.', 'Drivers on a budget.'),
        ('Carbon', 'A carbon film that won\'t fade and cuts more heat.', 'Keeps its colour and keeps the car cooler.', 'Daily drivers who want it to last.'),
        ('Ceramic', 'The top film for heat and glare rejection.', 'The coolest cabin and the least glare.', 'Long drives, families and anyone who wants the best.'),
        ('Sunstrip', 'A dark band across the top of the windscreen.', 'Cuts glare from a low sun.', 'Any car, often with a rear tint.')],
    'air-suspension': [
        ('Air Lift Performance 3P / 3H', 'Air suspension with height presets on your phone. 3H adds height sensors.', 'Low at a show, raised for speed bumps, at the touch of a button.', 'Show cars and daily drivers who want both looks and comfort.'),
        ('Prazis', 'Quality air kits that fit many cars.', 'Adjustable height for a wide range of cars.', 'Drivers whose car isn\'t covered by other kits.'),
        ('Boot builds', 'The air tanks and compressors fitted in the boot, on show or hidden.', 'Either part of the build or out of the way.', 'Show cars, or anyone who needs the boot space.')],
    'coilovers': [
        ('Coilovers', 'Suspension with adjustable height and damping.', 'Set the drop and the ride the way you want it.', 'Drivers who want a lower car and sharper handling.'),
        ('Lowering springs', 'Shorter springs for a fixed drop.', 'A simple, cheaper way to lower the car.', 'Drivers who want the look without adjusting it.')],
    'chrome-delete': [
        ('Window trims', 'The chrome around the windows wrapped black.', 'The biggest change for the money.', 'Anyone who wants a darker, sportier look.'),
        ('Grilles and badges', 'Front and rear grilles and badges, blacked out.', 'Finishes the look from the front and back.', 'Drivers going for a full black-out.')],
    'bodykits': [
        ('Spoilers and splitters', 'Rear spoilers and front splitters, fitted and lined up.', 'A sharper, lower look.', 'Drivers who want an aggressive stance.'),
        ('Side skirts and diffusers', 'Skirts along the sides and a diffuser at the back.', 'Makes the car look lower and wider.', 'Builds getting the full exterior treatment.'),
        ('Wide arch kits', 'Wider arches fitted to the body.', 'Room for wider wheels and a bold stance.', 'Show builds.')],
    'wheel-refurb': [
        ('Refurb', 'Kerb damage and corrosion repaired and refinished.', 'Wheels that look new again.', 'Anyone with scuffed or tired wheels.'),
        ('Colour change', 'Wheels refinished in any colour.', 'A big change to the car\'s look.', 'Drivers restyling their car.'),
        ('Caliper painting', 'Brake calipers painted in a heat-resistant finish.', 'A pop of colour behind the wheels.', 'Owners finishing off a build.')],
    'interiors': [
        ('Carbon trims', 'Carbon fibre trims for the dash and doors.', 'A sporty, premium finish inside.', 'Drivers who want the inside to match the outside.'),
        ('Alcantara', 'Alcantara on the headliner, trims or wheel.', 'Soft grip and a luxury feel.', 'Anyone upgrading the cabin.'),
        ('Steering wheels', 'Retrimmed or upgraded steering wheels.', 'The part you touch most, made better.', 'Drivers who want a sportier feel.'),
        ('Seats', 'Seats retrimmed or upgraded.', 'Comfort and a fresh look.', 'Worn interiors and full builds.')],
    'detailing': [
        ('Paint correction', 'Swirls and light scratches polished out, in three levels.', 'Brings back gloss and depth.', 'Cars with dull or swirled paint.'),
        ('Ceramic coating', 'A coating bonded to the paint.', 'Easier cleaning and gloss that lasts.', 'Owners who want the shine to stay.')],
    'number-plates': [
        ('Standard', 'Road-legal printed plates, made while you wait.', 'A quick, legal replacement.', 'Anyone with a damaged or missing plate.'),
        ('3D gel', 'Raised gel letters on a road-legal plate.', 'More depth and a premium look.', 'Drivers who want a step up from standard.'),
        ('4D laser-cut', 'Laser-cut raised letters.', 'Sharp, bold characters that stand out.', 'Drivers who want the boldest road-legal plate.'),
        ('Show plates', 'Custom plates for shows only, not the road.', 'Your own design for display.', 'Show cars and meets.')],
    'van-signage': [
        ('Lettering and logos', 'Your name, logo and number cut in vinyl.', 'Turns the van into an advert wherever it parks.', 'Small businesses and trades.'),
        ('Part wraps', 'Printed graphics on part of the van.', 'Big impact for less than a full wrap.', 'Businesses that want to be seen.'),
        ('Full livery', 'The whole van wrapped in your design.', 'Maximum branding and the paint underneath is protected.', 'Fleets and growing businesses.')],
}

# v5.5: guide chips link to the live blog posts (new site will move them to /blog/<slug> with redirects)
_BLOG_SLUG = {'Ghost immobiliser:': 'ghost-immobiliser-south-london-cost-fitting-is-it-worth-it', 'Why every London': 'why-every-london-car-owner-needs-security-right-now',
    'Best dash cam': 'best-dash-cam-2026-front-rear-gps-why-you-need-one', 'Apple CarPlay': 'apple-carplay-installation-south-london-hyped-up',
    'Car audio upgrade': 'car-audio-upgrade-premium-sound-with-subwoofers-lighting', 'ECU remapping': 'ecu-remapping-boost-power-efficiency-safely',
    'Car tuning in London': 'car-tuning-in-london-how-to-pick-a-safe-tuner', 'The legal reality': 'the-legal-reality-of-car-mods-in-the-uk-what-dvla-actually-cares',
    'How much does a car wrap': 'how-much-does-a-car-wrap-cost-uk-real-prices-not-marketing', 'Wrapping, PPF': 'vehicle-wrapping-ppf-window-tints-dechroming-signage',
    'The low life': 'the-low-life-chose-me-why-air-suspension-changed-everything', 'Air suspension and bodykit': 'air-suspension-bodykit-fitting-perfect-your-stance',
    'Car detailing': 'car-detailing-paint-correction-ceramic-coating', 'Custom number plates': 'custom-number-plates-in-london-same-day-service-styles',
    'Number plate cloning': 'number-plate-cloning-is-surging-how-to-protect-yourself'}
for _v in S.values():
    _v['blog'] = [(t, next(('https://hypedup.uk/hyped-up/f/' + sl for k, sl in _BLOG_SLUG.items() if t.startswith(k)), u)) for t, u in _v.get('blog', [])]
