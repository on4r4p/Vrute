import pycipher
import time
lst = ['hiboux','chouette','signature','linkenfant','lenfant','jungle','vavoir','excuseme','wellexcuseme','todown','toload','load','zero','cigar','nearfrom','nearthe','history','histoire','luck','goodluck','withluck','fantome','histoire','couloir','adrenaline','entite','deite','divinite','trinqu','trinquons','trinquer','culprit','gamepedia','singleplayer','illusion','faible','motivation','motiver','locomotive','motive','TRIA', 'TRIABLE', 'TRIABLES', 'TRIAC', 'TRIACANTHE', 'TRIACANTHES', 'TRIACASTELA', 'TRIACHAINE', 'TRIACHAINES', 'TRIACIDE', 'TRIACIDES', 'TRIACIDITE', 'TRIACIDITES', 'TRIACLAUTRAIT', 'TRIACLEUR', 'TRIACLEURS', 'TRIACONTAEDRE', 'TRIACONTAEDRES', 'TRIACONTANE', 'TRIACONTANES', 'TRIACS', 'TRIADE', 'TRIADELPHE', 'TRIADELPHES', 'TRIADENC', 'TRIADENCQUE', 'TRIADENCQUES', 'TRIADENCS', 'TRIADES', 'TRIADIMEFON', 'TRIADIMENOL', 'TRIADIQUE', 'TRIADIQUES', 'TRIAGE', 'TRIAGES', 'TRIAI', 'TRIAIENT', 'TRIAILLE', 'TRIAILLES', 'TRIAIRE', 'TRIAIRES', 'TRIAIS', 'TRIAISE', 'TRIAISES', 'TRIAIT', 'TRIAIZE', 'TRIAKENE', 'TRIAL', 'TRIALCOOL', 'TRIALCOOLS', 'TRIALISTE', 'TRIALISTES', 'TRIALLATE', 'TRIALLE', 'TRIALLES', 'TRIALOGUE', 'TRIALOGUES', 'TRIALS', 'TRIALUMINIQUE', 'TRIALUMINIQUES', 'TRIAMCINOLONE', 'TRIAMCINOLONES', 'TRIAMES', 'TRIAMMONIQUE', 'TRIAMMONIQUES', 'TRIANDINE', 'TRIANDINES', 'TRIANDRE', 'TRIANDRES', 'TRIANDRIE', 'TRIANDRIES', 'TRIANDRIQUE', 'TRIANDRIQUES', 'TRIANE', 'TRIANELLE', 'TRIANELLES', 'TRIANES', 'TRIANGLE', 'TRIANGLES', 'TRIANGULA', 'TRIANGULAI', 'TRIANGULAIENT', 'TRIANGULAIRE', 'TRIANGULAIREMENT', 'TRIANGULAIRES', 'TRIANGULAIS', 'TRIANGULAIT', 'TRIANGULAMES', 'TRIANGULANT', 'TRIANGULARITE', 'TRIANGULARITES', 'TRIANGULAS', 'TRIANGULASSE', 'TRIANGULASSENT', 'TRIANGULASSES', 'TRIANGULASSIEZ', 'TRIANGULASSIONS', 'TRIANGULAT', 'TRIANGULATES', 'TRIANGULATEUR', 'TRIANGULATION', 'TRIANGULATIONS', 'TRIANGULE', 'TRIANGULEE', 'TRIANGULEES', 'TRIANGULENT', 'TRIANGULER', 'TRIANGULERA', 'TRIANGULERAI', 'TRIANGULERAIENT', 'TRIANGULERAIS', 'TRIANGULERAIT', 'TRIANGULERAS', 'TRIANGULERENT', 'TRIANGULEREZ', 'TRIANGULERIEZ', 'TRIANGULERIONS', 'TRIANGULERONS', 'TRIANGULERONT', 'TRIANGULES', 'TRIANGULEZ', 'TRIANGULIEZ', 'TRIANGULIONS', 'TRIANGULONS', 'TRIANIEN', 'TRIANIENNE', 'TRIANIENNES', 'TRIANIENS', 'TRIANON', 'TRIANT', 'TRIAPENTHENOL', 'TRIAPERTURE', 'TRIARCHIE', 'TRIARCHIES', 'TRIARDS', 'TRIARGENTIQUE', 'TRIARGENTIQUES', 'TRIARYLAMINE', 'TRIARYLAMINES', 'TRIAS', 'TRIASIQUE', 'TRIASIQUES', 'TRIASSE', 'TRIASSENT', 'TRIASSES', 'TRIASSIEZ', 'TRIASSIONS', 'TRIASULFURON', 'TRIAT', 'TRIATES', 'TRIATHLETE', 'TRIATHLETES', 'TRIATHLON', 'TRIATHLONIEN', 'TRIATHLONIENNE', 'TRIATHLONIENNES', 'TRIATHLONIENS', 'TRIATHLONS', 'TRIATOME', 'TRIATOMES', 'TRIATOMICITE', 'TRIATOMICITES', 'TRIATOMINE', 'TRIATOMINES', 'TRIATOMIQUE', 'TRIATOMIQUES', 'TRIAU', 'TRIAUCOURT', 'TRIAULA', 'TRIAULAI', 'TRIAULAIENT', 'TRIAULAIS', 'TRIAULAIT', 'TRIAULAMES', 'TRIAULANT', 'TRIAULAS', 'TRIAULASSE', 'TRIAULASSENT', 'TRIAULASSES', 'TRIAULASSIEZ', 'TRIAULASSIONS', 'TRIAULAT', 'TRIAULATES', 'TRIAULE', 'TRIAULENT', 'TRIAULER', 'TRIAULERA', 'TRIAULERAI', 'TRIAULERAIENT', 'TRIAULERAIS', 'TRIAULERAIT', 'TRIAULERAS', 'TRIAULERENT', 'TRIAULEREZ', 'TRIAULERIEZ', 'TRIAULERIONS', 'TRIAULERONS', 'TRIAULERONT', 'TRIAULES', 'TRIAULEZ', 'TRIAULIEZ', 'TRIAULIONS', 'TRIAULONS', 'TRIAURIQUE', 'TRIAURIQUES', 'TRIAUX', 'TRIAZAMATE', 'TRIAZINE', 'TRIAZINES', 'TRIAZOLAM', 'TRIAZOLE', 'TRIAZOPHOS', 'TRIAZOXIDE', 'TRIBADA', 'TRIBADAI', 'TRIBADAIENT', 'TRIBADAIS', 'TRIBADAIT', 'TRIBADAMES', 'TRIBADANT', 'TRIBADAS', 'TRIBADASSE', 'TRIBADASSENT', 'TRIBADASSES', 'TRIBADASSIEZ', 'TRIBADASSIONS', 'TRIBADAT', 'TRIBADATES', 'TRIBADE', 'TRIBADENT', 'TRIBADER', 'TRIBADERA', 'TRIBADERAI', 'TRIBADERAIENT', 'TRIBADERAIS', 'TRIBADERAIT', 'TRIBADERAS', 'TRIBADERENT', 'TRIBADEREZ', 'TRIBADERIEZ', 'TRIBADERIONS', 'TRIBADERONS', 'TRIBADERONT', 'TRIBADES', 'TRIBADEZ', 'TRIBADIE', 'TRIBADIES', 'TRIBADIEZ', 'TRIBADIONS', 'TRIBADISME', 'TRIBADISMES', 'TRIBADONS', 'TRIBAL', 'TRIBALDOS', 'TRIBALE', 'TRIBALES', 'TRIBALISA', 'TRIBALISAI', 'TRIBALISAIENT', 'TRIBALISAIS', 'TRIBALISAIT', 'TRIBALISAMES', 'TRIBALISANT', 'TRIBALISAS', 'TRIBALISASSE', 'TRIBALISASSENT', 'TRIBALISASSES', 'TRIBALISASSIEZ', 'TRIBALISASSIONS', 'TRIBALISAT', 'TRIBALISATES', 'TRIBALISATION', 'TRIBALISATIONS', 'TRIBALISE', 'TRIBALISEE', 'TRIBALISEES', 'TRIBALISENT', 'TRIBALISER', 'TRIBALISERA', 'TRIBALISERAI', 'TRIBALISERAIENT', 'TRIBALISERAIS', 'TRIBALISERAIT', 'TRIBALISERAS', 'TRIBALISERENT', 'TRIBALISEREZ', 'TRIBALISERIEZ', 'TRIBALISERIONS', 'TRIBALISERONS', 'TRIBALISERONT', 'TRIBALISES', 'TRIBALISEZ', 'TRIBALISIEZ', 'TRIBALISIONS', 'TRIBALISME', 'TRIBALISMES', 'TRIBALISONS', 'TRIBALISTE', 'TRIBALISTES', 'TRIBALLA', 'TRIBALLAI', 'TRIBALLAIENT', 'TRIBALLAIS', 'TRIBALLAIT', 'TRIBALLAMES', 'TRIBALLANT', 'TRIBALLAS', 'TRIBALLASSE', 'TRIBALLASSENT', 'TRIBALLASSES', 'TRIBALLASSIEZ', 'TRIBALLASSIONS', 'TRIBALLAT', 'TRIBALLATES', 'TRIBALLE', 'TRIBALLEE', 'TRIBALLEES', 'TRIBALLENT', 'TRIBALLER', 'TRIBALLERA', 'TRIBALLERAI', 'TRIBALLERAIENT', 'TRIBALLERAIS', 'TRIBALLERAIT', 'TRIBALLERAS', 'TRIBALLERENT', 'TRIBALLEREZ', 'TRIBALLERIEZ', 'TRIBALLERIONS', 'TRIBALLERONS', 'TRIBALLERONT', 'TRIBALLES', 'TRIBALLEZ', 'TRIBALLIEZ', 'TRIBALLIONS', 'TRIBALLONS', 'TRIBALS', 'TRIBANO', 'TRIBART', 'TRIBARTS', 'TRIBARYTIQUE', 'TRIBARYTIQUES', 'TRIBASICITE', 'TRIBASICITES', 'TRIBASIQUE', 'TRIBASIQUES', 'TRIBATON', 'TRIBATONS', 'TRIBAUX', 'TRIBEHOU', 'TRIBENURONMETHYLE', 'TRIBETON', 'TRIBETONS', 'TRIBIANO', 'TRIBOELECTRICITE', 'TRIBOELECTRICITES', 'TRIBOELECTRIQUE', 'TRIBOELECTRIQUES', 'TRIBOGNA', 'TRIBOLOGIE', 'TRIBOLOGIES', 'TRIBOLOGIQUE', 'TRIBOLOGIQUES', 'TRIBOLUMINESCENCE', 'TRIBOLUMINESCENCES', 'TRIBOLUMINESCENT', 'TRIBOLUMINESCENTS', 'TRIBOMETRE', 'TRIBOMETRES', 'TRIBOMETRIE', 'TRIBOMETRIES', 'TRIBOMETRIQUE', 'TRIBOMETRIQUES', 'TRIBON', 'TRIBONIEN', 'TRIBONS', 'TRIBORD', 'TRIBORDAIS', 'TRIBORDS', 'TRIBOUDAIS', 'TRIBOUDAISE', 'TRIBOUDAISES', 'TRIBOUIL', 'TRIBOUILLA', 'TRIBOUILLAI', 'TRIBOUILLAIENT', 'TRIBOUILLAIS', 'TRIBOUILLAIT', 'TRIBOUILLAMES', 'TRIBOUILLANT', 'TRIBOUILLAS', 'TRIBOUILLASSE', 'TRIBOUILLASSENT', 'TRIBOUILLASSES', 'TRIBOUILLASSIEZ', 'TRIBOUILLASSIONS', 'TRIBOUILLAT', 'TRIBOUILLATES', 'TRIBOUILLE', 'TRIBOUILLEE', 'TRIBOUILLEES', 'TRIBOUILLENT', 'TRIBOUILLER', 'TRIBOUILLERA', 'TRIBOUILLERAI', 'TRIBOUILLERAIENT', 'TRIBOUILLERAIS', 'TRIBOUILLERAIT', 'TRIBOUILLERAS', 'TRIBOUILLERENT', 'TRIBOUILLEREZ', 'TRIBOUILLERIEZ', 'TRIBOUILLERIONS', 'TRIBOUILLERONS', 'TRIBOUILLERONT', 'TRIBOUILLES', 'TRIBOUILLEZ', 'TRIBOUILLIEZ', 'TRIBOUILLIONS', 'TRIBOUILLONS', 'TRIBOULA', 'TRIBOULAI', 'TRIBOULAIENT', 'TRIBOULAIS', 'TRIBOULAIT', 'TRIBOULAMES', 'TRIBOULANT', 'TRIBOULAS', 'TRIBOULASSE', 'TRIBOULASSENT', 'TRIBOULASSES', 'TRIBOULASSIEZ', 'TRIBOULASSIONS', 'TRIBOULAT', 'TRIBOULATES', 'TRIBOULE', 'TRIBOULEE', 'TRIBOULEES', 'TRIBOULENT', 'TRIBOULER', 'TRIBOULERA', 'TRIBOULERAI', 'TRIBOULERAIENT', 'TRIBOULERAIS', 'TRIBOULERAIT', 'TRIBOULERAS', 'TRIBOULERENT', 'TRIBOULEREZ', 'TRIBOULERIEZ', 'TRIBOULERIONS', 'TRIBOULERONS', 'TRIBOULERONT', 'TRIBOULES', 'TRIBOULET', 'TRIBOULETS', 'TRIBOULEZ', 'TRIBOULIEZ', 'TRIBOULIONS', 'TRIBOULOIS', 'TRIBOULOISE', 'TRIBOULOISES', 'TRIBOULONS', 'TRIBRAQUE', 'TRIBRAQUES', 'TRIBSEES', 'TRIBU', 'TRIBULATION', 'TRIBULATIONS', 'TRIBULE', 'TRIBULES', 'TRIBULI', 'TRIBUN', 'TRIBUNAL', 'TRIBUNAT', 'TRIBUNATS', 'TRIBUNAUX', 'TRIBUNE', 'TRIBUNES', 'TRIBUNICIEN', 'TRIBUNICIENNE', 'TRIBUNICIENNES', 'TRIBUNICIENS', 'TRIBUNIER', 'TRIBUNIERS', 'TRIBUNITIEN', 'TRIBUNITIENNE', 'TRIBUNITIENNES', 'TRIBUNITIENS', 'TRIBUNS', 'TRIBUS', 'TRIBUT', 'TRIBUTAIRE', 'TRIBUTAIRES', 'TRIBUTE', 'TRIBUTES', 'TRIBUTIF', 'TRIBUTIFS', 'TRIBUTIVE', 'TRIBUTIVES', 'TRIBUTS', 'TRIBUTYRINE', 'TRIBUTYRINES', 'TRIC', 'TRICAGE', 'TRICAGES', 'TRICALCIQUE', 'TRICALCIQUES', 'TRICAMERAL', 'TRICAMERALE', 'TRICAMERALES', 'TRICAMERAUX', 'TRICANDILLE', 'TRICANDILLES', 'TRICAPSULAIRE', 'TRICAPSULAIRES', 'TRICAR', 'TRICARBOXYLIQUE', 'TRICARBOXYLIQUES', 'TRICARD', 'TRICARDE', 'TRICARDES', 'TRICARDS', 'TRICARICO', 'TRICARRA', 'TRICARRAI', 'TRICARRAIENT', 'TRICARRAIS', 'TRICARRAIT', 'TRICARRAMES', 'TRICARRANT', 'TRICARRAS', 'TRICARRASSE', 'TRICARRASSENT', 'TRICARRASSES', 'TRICARRASSIEZ', 'TRICARRASSIONS', 'TRICARRAT', 'TRICARRATES', 'TRICARRE', 'TRICARREE', 'TRICARREES', 'TRICARRENT', 'TRICARRER', 'TRICARRERA', 'TRICARRERAI', 'TRICARRERAIENT', 'TRICARRERAIS', 'TRICARRERAIT', 'TRICARRERAS', 'TRICARRERENT', 'TRICARREREZ', 'TRICARRERIEZ', 'TRICARRERIONS', 'TRICARRERONS', 'TRICARRERONT', 'TRICARRES', 'TRICARREZ', 'TRICARRIEZ', 'TRICARRIONS', 'TRICARRONS', 'TRICARS', 'TRICARTE', 'TRICARTES', 'TRICASE', 'TRICASTIN', 'TRICASTINE', 'TRICASTINES', 'TRICASTINS', 'TRICENAIRE', 'TRICENAIRES', 'TRICENNAL', 'TRICENNALE', 'TRICENNALES', 'TRICENNAUX', 'TRICENTENAIRE', 'TRICENTENAIRES', 'TRICEPHALE', 'TRICEPHALES', 'TRICEPS', 'TRICERATOPS', 'TRICERRO', 'TRICESIMO', 'TRICETTE', 'TRICETTES', 'TRICHA', 'TRICHABLE', 'TRICHABLES', 'TRICHAI', 'TRICHAIENT', 'TRICHAIS', 'TRICHAIT', 'TRICHAMES', 'TRICHANT', 'TRICHAS', 'TRICHASSE', 'TRICHASSENT', 'TRICHASSES', 'TRICHASSIEZ', 'TRICHASSIONS', 'TRICHAT', 'TRICHATES', 'TRICHE', 'TRICHEE', 'TRICHEES', 'TRICHENT', 'TRICHER', 'TRICHERA', 'TRICHERAI', 'TRICHERAIENT', 'TRICHERAIS', 'TRICHERAIT', 'TRICHERAS', 'TRICHERENT', 'TRICHEREZ', 'TRICHERIE', 'TRICHERIES', 'TRICHERIEZ', 'TRICHERIONS', 'TRICHERONS', 'TRICHERONT', 'TRICHES', 'TRICHEUR', 'TRICHEURS', 'TRICHEUSE', 'TRICHEUSES', 'TRICHEY', 'TRICHEZ', 'TRICHIANA', 'TRICHIASE', 'TRICHIASES', 'TRICHIASIS', 'TRICHIEZ', 'TRICHINAL', 'TRICHINALE', 'TRICHINALES', 'TRICHINAUX', 'TRICHINE', 'TRICHINEE', 'TRICHINEES', 'TRICHINELLOSE', 'TRICHINELLOSES', 'TRICHINES', 'TRICHINEUSE', 'TRICHINEUSES', 'TRICHINEUX', 'TRICHINOSE', 'TRICHINOSES', 'TRICHIONS', 'TRICHISME', 'TRICHISMES', 'TRICHITE', 'TRICHITES', 'TRICHIURE', 'TRICHIURES', 'TRICHIURIDE', 'TRICHIURIDES', 'TRICHLO', 'TRICHLORACETIQUE', 'TRICHLORACETIQUES', 'TRICHLORE', 'TRICHLOREE', 'TRICHLOREES', 'TRICHLORES', 'TRICHLORETHENE', 'TRICHLORETHENES', 'TRICHLORETHYLENE', 'TRICHLORETHYLENES', 'TRICHLORFON', 'TRICHLOROETHENE', 'TRICHLOROETHENES', 'TRICHLOROETHYLENE', 'TRICHLOROETHYLENES', 'TRICHLORONATE', 'TRICHLORONITROMETHANE', 'TRICHLOROTRINITROBENZENE', 'TRICHLORURE', 'TRICHLORURES', 'TRICHLOS', 'TRICHOBEZOAIRE', 'TRICHOBEZOAIRES', 'TRICHOBEZOARD', 'TRICHOBEZOARDS', 'TRICHOBLASTE', 'TRICHOBLASTES', 'TRICHOCARDIE', 'TRICHOCARDIES', 'TRICHOCEPHALE', 'TRICHOCEPHALES', 'TRICHOCEPHALOSE', 'TRICHOCERIDE', 'TRICHOCERIDES', 'TRICHOCYSTE', 'TRICHOCYSTES', 'TRICHODESMIUM', 'TRICHODESMIUMS', 'TRICHODONTE', 'TRICHOGLOSSIE', 'TRICHOGLOSSIES', 'TRICHOGRAMME', 'TRICHOGRAMMES', 'TRICHOLOGIE', 'TRICHOLOGIES', 'TRICHOLOMATACEE', 'TRICHOLOMATACEES', 'TRICHOLOME', 'TRICHOLOMES', 'TRICHOMA', 'TRICHOMANE', 'TRICHOMANES', 'TRICHOMANIE', 'TRICHOMANIES', 'TRICHOMAS', 'TRICHOMATEUX', 'TRICHOMATIQUE', 'TRICHOMATIQUES', 'TRICHOME', 'TRICHOMES', 'TRICHOMONAS', 'TRICHONOSE', 'TRICHONOSES', 'TRICHONS', 'TRICHOPATHIE', 'TRICHOPATHIES', 'TRICHOPHOBIE', 'TRICHOPHOBIES', 'TRICHOPHYTIE', 'TRICHOPHYTIES', 'TRICHOPHYTON', 'TRICHOPHYTONS', 'TRICHOPTERE', 'TRICHOPTERES', 'TRICHOPYRITE', 'TRICHOPYRITES', 'TRICHORHIZE', 'TRICHORHIZES', 'TRICHORRHIZE', 'TRICHORRHIZES', 'TRICHOSANIQUE', 'TRICHOSANIQUES', 'TRICHOSANTHE', 'TRICHOSANTHES', 'TRICHOSCOPE', 'TRICHOSCOPES', 'TRICHOSCOPIQUE', 'TRICHOSCOPIQUES', 'TRICHOSE', 'TRICHOSES', 'TRICHOSIS', 'TRICHOSOME', 'TRICHOTA', 'TRICHOTAI', 'TRICHOTAIENT', 'TRICHOTAIS', 'TRICHOTAIT', 'TRICHOTAMES', 'TRICHOTANT', 'TRICHOTAS', 'TRICHOTASSE', 'TRICHOTASSENT', 'TRICHOTASSES', 'TRICHOTASSIEZ', 'TRICHOTASSIONS', 'TRICHOTAT', 'TRICHOTATES', 'TRICHOTE', 'TRICHOTEE', 'TRICHOTEES', 'TRICHOTENT', 'TRICHOTER', 'TRICHOTERA', 'TRICHOTERAI', 'TRICHOTERAIENT', 'TRICHOTERAIS', 'TRICHOTERAIT', 'TRICHOTERAS', 'TRICHOTERENT', 'TRICHOTEREZ', 'TRICHOTERIEZ', 'TRICHOTERIONS', 'TRICHOTERONS', 'TRICHOTERONT', 'TRICHOTES', 'TRICHOTETRATOMIE', 'TRICHOTETRATOMIES', 'TRICHOTEZ', 'TRICHOTIEZ', 'TRICHOTILLOMANIE', 'TRICHOTILLOMANIES', 'TRICHOTIN', 'TRICHOTINE', 'TRICHOTINES', 'TRICHOTINS', 'TRICHOTIONS', 'TRICHOTOME', 'TRICHOTOMES', 'TRICHOTOMIE', 'TRICHOTOMIES', 'TRICHOTOMIQUE', 'TRICHOTONS', 'TRICHROISME', 'TRICHROISMES', 'TRICHROITE', 'TRICHROITES', 'TRICHROMATE', 'TRICHROMATES', 'TRICHROMATIE', 'TRICHROMATIES', 'TRICHROMATISME', 'TRICHROMATISMES', 'TRICHROMATOPSIE', 'TRICHROMATOPSIES', 'TRICHROME', 'TRICHROMES', 'TRICHROMIE', 'TRICHROMIES', 'TRICHT', 'TRICIO', 'TRICK', 'TRICKS', 'TRICKSTER', 'TRICKSTERS', 'TRICLINIA', 'TRICLINIQUE', 'TRICLINIQUES', 'TRICLINIUM', 'TRICLINIUMS', 'TRICLOPYR', 'TRICLOSAN', 'TRICLOSANS', 'TRICOBALTIQUE', 'TRICOBALTIQUES', 'TRICOCHE', 'TRICOCHES', 'TRICOEUR', 'TRICOEURS', 'TRICOISE', 'TRICOISES', 'TRICOL', 'TRICOLA', 'TRICOLAI', 'TRICOLAIENT', 'TRICOLAIS', 'TRICOLAIT', 'TRICOLAMES', 'TRICOLANT', 'TRICOLAS', 'TRICOLASSE', 'TRICOLASSENT', 'TRICOLASSES', 'TRICOLASSIEZ', 'TRICOLASSIONS', 'TRICOLAT', 'TRICOLATES', 'TRICOLE', 'TRICOLENT', 'TRICOLER', 'TRICOLERA', 'TRICOLERAI', 'TRICOLERAIENT', 'TRICOLERAIS', 'TRICOLERAIT', 'TRICOLERAS', 'TRICOLERENT', 'TRICOLEREZ', 'TRICOLERIEZ', 'TRICOLERIONS', 'TRICOLERONS', 'TRICOLERONT', 'TRICOLES', 'TRICOLEZ', 'TRICOLIEZ', 'TRICOLIONS', 'TRICOLONS', 'TRICOLOR', 'TRICOLORA', 'TRICOLORAI', 'TRICOLORAIENT', 'TRICOLORAIS', 'TRICOLORAIT', 'TRICOLORAMES', 'TRICOLORANT', 'TRICOLORAS', 'TRICOLORASSE', 'TRICOLORASSENT', 'TRICOLORASSES', 'TRICOLORASSIEZ', 'TRICOLORASSIONS', 'TRICOLORAT', 'TRICOLORATES', 'TRICOLORE', 'TRICOLOREE', 'TRICOLOREES', 'TRICOLORENT', 'TRICOLORER', 'TRICOLORERA', 'TRICOLORERAI', 'TRICOLORERAIENT', 'TRICOLORERAIS', 'TRICOLORERAIT', 'TRICOLORERAS', 'TRICOLORERENT', 'TRICOLOREREZ', 'TRICOLORERIEZ', 'TRICOLORERIONS', 'TRICOLORERONS', 'TRICOLORERONT', 'TRICOLORES', 'TRICOLOREZ', 'TRICOLORIEZ', 'TRICOLORIONS', 'TRICOLORONS', 'TRICON', 'TRICONE', 'TRICONES', 'TRICONS', 'TRICONTINENTAL', 'TRICONTINENTALE', 'TRICONTINENTAUX', 'TRICOPTERE', 'TRICOPTERES', 'TRICOQUE', 'TRICOQUES', 'TRICORDE', 'TRICORDES', 'TRICORE', 'TRICORES', 'TRICORNE', 'TRICORNES', 'TRICORPS', 'TRICOSANE', 'TRICOSANES', 'TRICOSINE', 'TRICOSTE', 'TRICOT', 'TRICOTA', 'TRICOTAGE', 'TRICOTAGES', 'TRICOTAI', 'TRICOTAIENT', 'TRICOTAIS', 'TRICOTAIT', 'TRICOTAMES', 'TRICOTANT', 'TRICOTAS', 'TRICOTASSE', 'TRICOTASSENT', 'TRICOTASSES', 'TRICOTASSIEZ', 'TRICOTASSIONS', 'TRICOTAT', 'TRICOTATES', 'TRICOTE', 'TRICOTEE', 'TRICOTEES', 'TRICOTENT', 'TRICOTER', 'TRICOTERA', 'TRICOTERAI', 'TRICOTERAIENT', 'TRICOTERAIS', 'TRICOTERAIT', 'TRICOTERAS', 'TRICOTERENT', 'TRICOTEREZ', 'TRICOTERIE', 'TRICOTERIES', 'TRICOTERIEZ', 'TRICOTERIONS', 'TRICOTERONS', 'TRICOTERONT', 'TRICOTES', 'TRICOTET', 'TRICOTETS', 'TRICOTEUR', 'TRICOTEURS', 'TRICOTEUSE', 'TRICOTEUSES', 'TRICOTEZ', 'TRICOTIEZ', 'TRICOTIN', 'TRICOTINS', 'TRICOTIONS', 'TRICOTIS', 'TRICOTOIS', 'TRICOTOISE', 'TRICOTOISES', 'TRICOTONS', 'TRICOTS', 'TRICOTTER', 'TRICOUNI', 'TRICOUNIS', 'TRICOURANT', 'TRICS', 'TRICTRAC', 'TRICTRACS', 'TRICUIVRIQUE', 'TRICUIVRIQUES', 'TRICUSPIDE', 'TRICUSPIDES', 'TRICYCLA','trigono','trigonometrie','trigonometry','tricrypt','trigame','tricolor','badguy','balade','blabla','down','tweak','howto','youtube','parlant','parler','parle','diagenese','genese','digest','hexdigest','indestructible','destruct','impossible','domestic','domestique','phoenix','supermario','mariobros','icould','couldsay','expliqu','explication','contrefacon','passorcier','algorythme','algebre','ambigu','golem','legolem','ungolem','angoulem','responsable','verify','justicier','justice','chateau','forteresse','frequence','index','tropgaffe','pastrop','nefaite','precedent','zeldaetganon','combo','rusepour','ilfautetre','templede','ilfallait','racconte','cosplaye','cosplay','zeldagame','sagazelda','zeldasaga','quelquun','quelque','meilleur','ailleur','gnome','fortcommeunboeuf','fortcomme','boeuf','clown','supersmash','alabonneheure','situveu','second','bonheur','ilest','lownrj','lowenerg','lowenergie','ilpeut','quipeut','quiveux','voeux','tuveux','sivous','toique','toiquiveux','toiqui','toikiva','toikive','verifie','goal','tribulation','moimeme','renseigne','crucifix','hacking','hacker','gameboycolor','apprendre','program','progr','cettefois','biencettefois','boncettefois','popcorn','ducoups','important','salut','newyork','graal','saintgraal','jeanpierre','equipier','equip','equipement','obtenir','pourquoi','alors','accident','rupee','animationmagic','zeldagame','capcom','sortisur','sortien','quatrevingt','milleneufcentving','neufcent','milleneuf','quatre','cinq','sept','neuf','sursnes','delasnes','lasnes','snes','amateur','kidnap','kidnaping','meticuleux','ridiculous','ridicule','aubout','altgr','proverbe','silvousplait','please','charger','willbe','nonmerci','observation','observe',"seuil",'solaire','luciole','realisa','sacrifi','sacrifice','attendez','dunbaton','msdos','youlearn','appliquer','seeyoulater','templier','granted','access','bingo',"formidable","ascii",'fleuron','jeveux','jepeux','collector','compromi','commepromi','newgamecrack','cracking','gamecrack','laforme','rejoins','justement','juste','area','whydoes','whyare','whydo','proteger','ellesappelle','ilya','indique','ahok','faites','jefais','jesais','desole','drole','brillament','brillant','lecoffre','pourouvrir','coffre','tresor','reflechir','nombre','ilfaudrait','excluant','technique','hercule','game','exceptionnelle','exceptionelle','exception','exemple','dernier','final','message','prive','homme','devant','aimable', 'aime', 'relever', 'des', 'defis', 'ambitieux', 'amical', 'applique', 'articule', 'artiste', 'assure', 'attentionne', 'autonome', 'bonne', 'resistance', 'au', 'stress', 'calme', 'competent', 'comprehensif', 'consciencieux', 'consequent', 'creatif', 'curieux', 'delicat', 'determine', 'devoue', 'digne', 'de', 'confiance', 'diplomate', 'doue', 'efficace', 'enthousiaste', 'esprit', 'analyse', 'esprit', "equipe", 'esprit', 'de', 'competition', 'esprit', 'scientifique', 'fiable', 'honnete', 'imaginatif', 'ingenieux', 'innovateur', 'inventif', 'logique', 'loyal', 'meticuleux', 'minutieux', 'novateur', 'optimiste', 'organise', 'original', 'ouvert', 'patient', 'perseverant', 'perspicace', 'persuasif', 'poli', 'ponctuel', 'positif', 'pratique', 'precis', 'prevenant', 'prevoyant', 'prudent', 'reflechi', 'responsable', "adapte", 'facilement', 'sens', 'de', "lhumour", 'serieux', 'sincere', 'sociable', 'souple', 'spontane', 'stable', 'sympathique', 'tenace','perseverance','courage','patience','attaque','ordinateur','mais','encore','bientot','vigenere','mathgl','merci','animation','animateur','preuve','hoho','hihi','hehe','devez','termine','voila','fini','phrase','dechiffre','encoder','triforce','zelda','chiffrage','contest','newbie','difficile','super','cool','chiffrement','crypto','cryptographie','code','niveau','cette','sexy','jesperequ','epreuve','challenge','valider','super','felicitation','motdepasse','trouve','avez','vous','bravo','password','autre', 'apres', 'regarder', 'toujours', 'puis', 'jamais', 'cela', 'aimer', 'non', 'heure', 'croire', 'cent', 'monde', 'donc', 'enfant', 'fois', 'seul', 'autre', 'entre', 'vers', 'chez', 'demander', 'jeune', 'jusque', 'tres', 'moment', 'rester', 'repondre', 'tout', 'tete', 'pere', 'fille', 'mille', 'premier', 'car', 'entendre', 'ni', 'bon', 'trois', 'coeur', 'ainsi', 'an', 'quatre', 'un', 'terre', 'contre', 'dieu', 'monsieur', 'voix', 'penser', 'quel', 'arriver', 'maison', 'devant', 'coup', 'beau', 'connaitre', 'devenir', 'air', 'mot', 'nuit', 'sentir', 'eau', 'vieux', 'sembler', 'moins', 'tenir', 'ici', 'comprendre', 'oui', 'rendre', 'toi', 'vingt', 'depuis', 'attendre', 'sortir', 'ami', 'trop', 'porte', 'lequel', 'chaque', 'amour', 'pendant', 'deja', 'pied', 'tant', 'gens', 'parce que', 'nom', 'vivre', 'reprendre', 'entrer', 'porter', 'pays', 'ciel', 'avant', 'frere', 'regard', 'chercher', 'ame', 'cote', 'mort', 'revenir', 'noir', 'maintenant', 'nouveau', 'ville', 'rue', 'enfin', 'appeler', 'soir', 'chambre', 'mourir', 'pas', 'partir', 'cinq', 'esprit', 'soleil', 'dernier', 'jeter', 'dix', 'roi', 'etat', 'corps', 'beaucoup', 'suivre', 'bras', 'ecrire', 'blanc', 'montrer', 'tomber', 'place', 'ouvrir', 'ah', 'parti', 'assez', 'leur', 'cher', 'voila', 'annee', 'loin', 'point', 'visage', 'bruit', 'lettre', 'franc', 'fond', 'force', 'arreter', 'perdre', 'commencer', 'paraitre', 'aucun', 'marcher', 'milieu', 'saint', 'idee', 'presque', 'ailleurs', 'travail', 'lumiere', 'long', 'seulement', 'mois', 'fils', 'neuf', 'tel', 'lever', 'raison', 'effet', 'gouvernement', 'permettre', 'pauvre', 'asseoir', 'point', 'plein', 'personne', 'vrai', 'peuple', 'fait', 'parole', 'guerre', 'toute', 'ecouter', 'pensee', 'affaire', 'quoi', 'matin', 'pierre', 'monter', 'bas', 'vent', 'doute', 'front', 'ombre', 'part', 'maitre', 'aujourdhui', 'besoin', 'question', 'apercevoir', 'recevoir', 'mieux', 'peine', 'tour', 'servir', 'oh', 'autour', 'pres', 'finir', 'famille', 'pourquoi', 'souvent', 'rire', 'dessus', 'madame', 'sorte', 'figure', 'droit', 'peur', 'bout', 'lieu', 'silence', 'gros', 'chef', 'eh', 'six', 'bois', 'mari', 'histoire', 'crier', 'jouer', 'feu', 'tourner', 'doux', 'longtemps', 'fort', 'heureux', 'comme', 'garder', 'partie', 'face', 'mouvement', 'fin', 'reconnaitre', 'quitter', 'personne', 'comment', 'route', 'des', 'manger', 'livre', 'arbre', 'courir', 'cas', 'huit', 'lorsque', 'mur', 'ordre', 'continuer', 'bonheur', 'oublier', 'descendre', 'haut', 'interet', 'cacher', 'lun', 'chacun', 'profond', 'argent', 'cause', 'poser', 'autant', 'est', 'travers', 'grand', 'instant', 'facon', 'dabord', 'oeil', 'tirer', 'forme', 'presenter', 'ajouter', 'agir', 'retrouver', 'chemin', 'cheveu', 'offrir', 'surtout', 'certain', 'plaisir', 'suite', 'apprendre', 'malgre', 'tuer', 'rouge', 'sang', 'retourner', 'rencontrer', 'sentiment', 'fleur', 'cependant', 'service', 'plusieurs', 'table', 'vite', 'paix', 'envoyer', 'moyen', 'dormir', 'pousser', 'lit', 'humain', 'voiture', 'rappeler', 'etre', 'lire', 'general', 'nature', 'or', 'pouvoir', 'nouveau', 'francais', 'joie', 'sept', 'tard', 'president', 'pourtant', 'bouche', 'changer', 'petit', 'froid', 'compter', 'occuper', 'sens', 'cri', 'cheval', 'loi', 'sombre', 'ci', 'sur', 'espece', 'voici', 'ancien', 'tandis que', 'frapper', 'ministre', 'puisque', 'selon', 'travailler', 'expliquer', 'propre', 'obtenir', 'rentrer', 'mal', 'pleurer', 'essayer', 'repeter', 'societe', 'parfois', 'politique', 'oreille', 'payer', 'politique', 'apporter', 'fenetre', 'derriere', 'possible', 'fortune', 'compte', 'champ', 'manier', 'vraiment', 'immense', 'action', 'boire', 'public', 'garcon', 'pareil', 'bleu', 'sourire', 'couleur', 'coucher', 'papier', 'dautres', 'mal', 'fort', 'bientot', 'causer', 'piece', 'montagne', 'sol', 'oeuvre', 'partout', 'trente', 'exister', 'cours', 'raconter', 'serrer', 'songer', 'desir', 'manquer', 'cour', 'nommer', 'bord', 'douleur', 'conduire', 'salle', 'saisir', 'premier', 'comment', 'projet', 'demeurer', 'simple', 'etude', 'remettre', 'journal', 'geste', 'disparaitre', 'battre', 'toucher', 'situation', 'oiseau', 'necessaire', 'exemple', 'siecle', 'apparaitre', 'souffrir', 'million', 'prix', 'groupe', 'centre', 'malheur', 'honneur', 'fermer', 'accepter', 'garde', 'mauvais', 'tendre', 'naitre', 'sauver', 'entier', 'parmi', 'probleme', 'larme', 'avancer', 'chien', 'peau', 'reste', 'traverser', 'nombre', 'debout', 'mesure', 'social', 'souvenir', 'article', 'vue', 'couvrir', 'age', 'gagner', 'systeme', 'long', 'former', 'plaire', 'embrasser', 'reve', 'oser', 'afin de', 'passion', 'auquel', 'rapport', 'refuser', 'important', 'decider', 'produire', 'soldat', 'levre', 'signe', 'verite', 'charger', 'mariage', 'meler', 'certain', 'plan', 'cesser', 'ressembler', 'dos', 'marche', 'souvenir', 'dame', 'chanter', 'plutot', 'conseil', 'sou', 'triste', 'coin', 'jardin', 'joli', 'soit', 'empecher', 'doigt', 'objet', 'fer', 'lendemain', 'lentement', 'combien', 'approcher', 'prier', 'train', 'esperer', 'papa', 'different', 'valeur', 'jeu', 'echapper', 'glisser', 'secret', 'haut', 'vieillard', 'briller', 'docteur', 'bruler', 'terrible', 'placer', 'ton', 'jambe', 'juger', 'suffire', 'endroit', 'minute', 'atteindre', 'nuage', 'presence', 'fou', 'epaule', 'leger', 'feuille', 'liberte', 'journee', 'libre', 'annoncer', 'avenir', 'sourire', 'hier', 'resultat', 'elever', 'acheter', 'mener', 'preparer', 'pourquoi', 'hotel', 'semaine', 'foret', 'assurer', 'pur', 'qualite', 'prince', 'bien', 'egalement', 'deviner', 'medecin', 'considerer', 'volonte', 'seigneur', 'effort', 'quelque', 'vert', 'art', 'moindre', 'demain', 'quarante', 'cinquante', 'foule', 'appartenir', 'aussitot', 'ligne', 'representer', 'tromper', 'interieur', 'vendre', 'beaute', 'riche', 'craindre', 'etrange', 'emporter', 'ensuite', 'soin', 'naturel', 'hasard', 'puis', 'condition', 'quinze', 'classe', 'voyage', 'aupres', 'present', 'caractere', 'attention', 'gris', 'or', 'rouler', 'faible', 'posseder', 'scene', 'difficile', 'francais', 'reveiller', 'foi', 'aider', 'decouvrir', 'odeur', 'choisir', 'musique', 'oncle', 'evenement', 'prononcer', 'village', 'taire', 'envie', 'midi', 'ensemble', 'expression', 'herbe', 'vieux', 'pluie', 'pres', 'bas', 'rever', 'appuyer', 'etendre', 'apres', 'general', 'lutte', 'trembler', 'reponse', 'grace', 'espace', 'habitude', 'defendre', 'memoire', 'creer', 'grave', 'maintenir', 'verre', 'campagne', 'quelquun', 'juge', 'genou', 'impossible', 'fete', 'indiquer', 'pret', 'promettre', 'relever', 'abandonner', 'ignorer', 'large', 'parent', 'colere', 'exprimer', 'etoile', 'devoir', 'conscience', 'existence', 'accompagner', 'immobile', 'adresser', 'observer', 'juste', 'puissance', 'matiere', 'sable', 'separer', 'marier', 'prevoir', 'vivant', 'accord', 'hiver', 'retour', 'autrefois', 'genre', 'dautres', 'vif', 'amener', 'obliger', 'acte', 'image', 'horizon', 'eclairer', 'poursuivre', 'danger', 'livrer', 'role', 'escalier', 'gout', 'bete', 'ceci', 'recherche', 'membre', 'pain', 'phrase', 'contenir', 'rire', 'fuir', 'couler', 'terme', 'eaux', 'moyen', 'police', 'rocher', 'proposer', 'tranquille', 'unique', 'eprouver', 'retenir', 'type', 'vin', 'superieur', 'attacher', 'voler', 'sec', 'justice', 'epoque', 'passage', 'somme', 'science', 'surprendre', 'cote', 'doucement', 'gauche', 'faute', 'ecole', 'bon', 'ensemble', 'rayon', 'briser', 'sujet', 'imaginer', 'diriger', 'douze', 'en', 'lune', 'dernier', 'avis', 'parvenir', 'ouvert', 'penetrer', 'poete', 'meilleur', 'paysan', 'remarquer', 'chair', 'eviter', 'soudain', 'succes', 'ile', 'etablir', 'reussir', 'pencher', 'habiter', 'entourer', 'declarer', 'detail', 'arme', 'realite', 'confiance', 'masse', 'crise', 'etonner', 'poste', 'dresser', 'durer', 'depuis', 'FAUX', 'fixer', 'enorme', 'principe', 'direction', 'taille', 'desirer', 'sante', 'ventre', 'marche', 'puissant', 'simplement', 'environ', 'tellement', 'arracher', 'entrainer', 'soutenir', 'couper', 'trou', 'inconnu', 'pont', 'lune', 'dehors', 'certes', 'beaux', 'robe', 'douter', 'retirer', 'cesse', 'brusquement', 'entree', 'source', 'camarade', 'dent', 'quant a', 'connaissance', 'cou', 'but', 'promener', 'vague', 'element', 'fil', 'voie', 'nez', 'forcer', 'particulier', 'discours', 'maladie', 'chaleur', 'gloire', 'vide', 'examiner', 'revoir', 'aide', 'debut', 'ennemi', 'second', 'aile', 'flamme', 'chaise', 'lourd', 'sein', 'veritable', 'toit', 'remplir', 'terminer', 'vaste', 'denude', 'poussiere', 'nord', 'tenter', 'emotion', 'hors', 'un', 'remonter', 'revolution', 'theatre', 'armee', 'court', 'noir', 'appartement', 'semblable', 'installer', 'haine', 'jeune', 'position', 'seconde', 'frais', 'appel', 'soulever', 'espoir', 'allumer', 'imposer', 'avant', 'respirer', 'arriere', 'baisser', 'droite', 'poitrine', 'mort', 'jeunesse', 'bureau', 'sac', 'etranger', 'courage', 'souffler', 'jaune', 'page', 'etranger', 'etc', 'miser', 'passe', 'rapide', 'digne', 'chaud', 'propos', 'attirer', 'preter', 'clair', 'amuser', 'occasion', 'voile', 'eclater', 'importance', 'quartier', 'soi', 'auteur', 'religion', 'palais', 'reunir', 'traiter', 'flot', 'intelligence', 'tantot', 'voisin', 'carte', 'secret', 'animal', 'ete', 'trainer', 'cabinet', 'morceau', 'employer', 'capable', 'souffrance', 'marquer', 'prouver', 'importer', 'titre', 'desert', 'facile', 'spectacle', 'exiger', 'reposer', 'depart', 'fier', 'danser', 'demande', 'saluer', 'lueur', 'joue', 'saint', 'accorder', 'priere', 'achever', 'avouer', 'distinguer', 'emmener', 'fonction', 'durant', 'haut', 'aspect', 'sommeil', 'eclat', 'moitie', 'demi', 'calme', 'contraire', 'colline', 'agiter', 'hesiter', 'terrain', 'rare', 'poids', 'sonner', 'changement', 'charge', 'davantage', 'composer', 'enlever', 'poche', 'rejoindre', 'son', 'interieur', 'veille', 'ramener', 'fruit', 'complet', 'etudier', 'partager', 'croix', 'suivant', 'chasser', 'interrompre', 'eloigner', 'tresor', 'compagnie', 'etroit', 'cuisine', 'reduire', 'engager', 'egal', 'empire', 'nation', 'eteindre', 'recommencer', 'sauter', 'plaindre', 'conversation', 'soiree', 'violent', 'impression', 'trait', 'devant', 'preferer', 'reveler', 'sien', 'magnifique', 'desespoir', 'temoin', 'visite', 'respect', 'solitude', 'subir', 'dela', 'prochain', 'anglais', 'rapporter', 'couter', 'reflechir', 'officier', 'remercier', 'deposer', 'fauteuil', 'fumer', 'tot', 'affirmer', 'relation', 'fumee', 'convenir', 'branche', 'malade', 'circonstance', 'ouvrage', 'compagnon', 'vetir', 'experience', 'port', 'accomplir', 'avec', 'resoudre', 'plonger', 'goutte', 'mien', 'chant', 'detruire', 'combat', 'personnage', 'aventure', 'interesser', 'disposer', 'absence', 'machine', 'aucun', 'grace', 'chaine','louable','cepasse','lepasse','cepass','lepass','lecode','indice','melanger','biologie','fichier','telecharge','telecharger','rapide','cecode','jetoffre','paspasser','jevoudrai','jeveux','cruel','lumiere','examen','examine','lemdp','exclu','exclusif','decode','vicieux','pouvoir','sword','epee','donjon','relique','deesse','legend','courage','sagesse','force','devant','variante','qualite','homosexu','coeurloyal','manque','unbon','puissant','passant','trouve','lemot','moment','finalement','aufinal','facilement','passage','zodiac','coeur','resoudre','resolu','reussi','casser','bruteforce','complique','vertue','virtual','virtuel','possible','impossible','suppose','moral','moralite','facile','difficile','merci','vous','ceque','hyrule','passer','chemin','merite','entoutcas','limite','depasser','imagine','imagination','dessin','converti','decimal','jeuvideo','link','epona','ganondo','confirme','valid','passeur','attaque','problematique','probleme','probable','parcequ','google','okjecpas','okjecpassi','okjecpasce','methode','principe','principale','personnage','personne','video','animation','passe','dessinateur','passeest','dernier', 'final', 'message', 'prive', 'homme', 'devant', 'aimable', 'aime', 'relever', 'des', 'defis', 'ambitieux', 'amical', 'applique', 'articule', 'artiste', 'assure', 'attentionne', 'autonome', 'bonne', 'resistance', 'au', 'stress', 'calme', 'competent', 'comprehensif', 'consciencieux', 'consequent', 'creatif', 'curieux', 'delicat', 'determine', 'devoue','victoire','decision','decider','decide','decidement','dignede','etesdigne','esdigne','dignite', 'confiance', 'diplomate', 'doue', 'efficace', 'enthousiaste', 'esprit', 'analyse', 'esprit', 'equipe', 'esprit', 'de', 'competition', 'esprit', 'scientifique', 'fiable', 'honnete', 'imaginatif', 'ingenieux', 'innovateur', 'inventif', 'logique', 'loyal', 'meticuleux', 'minutieux', 'novateur', 'optimiste', 'organise', 'original', 'ouvert', 'patient', 'perseverant', 'perspicace', 'persuasif', 'poli', 'ponctuel', 'positif', 'pratique', 'precis', 'prevenant', 'prevoyant', 'prudent', 'reflechi', 'responsable', 'adapte', 'facilement', 'sens', 'de', 'lhumour', 'serieux', 'sincere', 'sociable', 'souple', 'spontane', 'stable', 'sympathique', 'tenace', 'perseverance', 'courage', 'patience', 'attaque', 'ordinateur', 'mais', 'encore', 'bientot', 'vigenere', 'mathgl', 'merci', 'animation', 'animateur', 'preuve', 'hoho', 'hihi', 'hehe', 'devez', 'termine', 'voila', 'fini', 'phrase', 'dechiffre', 'encoder', 'triforce', 'zelda', 'chiffrage', 'contest', 'newbie', 'difficile', 'superman', 'cool', 'chiffrement', 'crypto', 'cryptographie', 'code', 'niveau', 'cette', 'sexy', 'jesperequ', 'epreuve', 'challenge', 'valider','password','pour','bravo','www','okmerci','okmec','delta','quela','quele','chercher','newbie','arme','limonade','citron','marmelade','acide','macintosh','proteine','cestca','cestcela','comme','commecela','decodeur','abimer','codon','exode','grosses', 'version', 'compagnie', 'richard', 'internet', 'machine', 'produce', 'follows', 'grande', 'faciles', 'other', 'homme', 'actionrpg', 'watchtrois', 'statut', 'topped', 'acting', 'swords', 'decouvrant', 'endroits', 'team', 'trilogy', 'alongside', 'flash', 'frequemment', 'famitsu', 'fond', 'would', 'impraticables', 'container', 'record', 'datant', 'time', 'casey', 'actionadventure', 'nabooru', 'spirituelle', 'fitzgerald', 'lune', 'speak', 'restless', 'compositeurla', 'devenue', 'scott', 'japan', 'prequel', 'dura', 'space', 'anyone', 'bound', 'knowing', 'vingtquatre', 'looks', 'scellele', 'satellite', 'satellaview', 'male', 'gibdos', 'lambiance', 'reprend', 'engendrant', 'akito', 'kids', 'gaining', 'someone', 'molina', 'indispensable', 'mind', 'traditionnelle', 'owsen', 'sintitule', 'enter', 'platformer', 'thus', 'overhead', 'zeldaa', 'rapport', 'supposent', 'evolution', 'nourrissent', 'king', 'until', 'adventuresthe', 'effrois', 'ishikawa', 'adventure', 'serait', 'peignent', 'minutes', 'gamers', 'rupeeland', 'skimo', 'ruto', 'featuring', 'asks', 'wildsthe', 'elevees', 'croissant', 'serie', 'gamespys', 'aout', 'donjon', 'usual', 'compass', 'wrote', 'sailing', 'display', 'style', 'seamless', 'possesses', 'computer', 'intended', 'completed', 'face', 'directly', 'reduire', 'hourglassbilly', 'presentation', 'appeared', 'nombreux', 'classified', 'lenticular', 'names', 'sticker', 'majeure', 'spell', 'danse', 'interactions', 'incarne', 'iwata', 'passant', 'point', 'love', 'reliant', 'apparition', 'sometimes', 'breath', 'fitzgeralds', 'developing', 'satellitebased', 'listup', 'presentes', 'accession', 'releasing', 'prenait', 'mounted', 'stores', 'james', 'grace', 'sachant', 'shook', 'notably', 'euxmemes', 'manga', 'graeme', 'freedom', 'sworduniversimage', 'visqueuse', 'trouve', 'spinoffs', 'affirme', 'retrospective', 'connexion', 'development', 'lobjet', 'underground', 'celebrated', 'apprend', 'around', 'hack', 'royale', 'oiseaux', 'travailler', 'grown', 'lapparition', 'gallery', 'denfance', 'nouveautes', 'assassins', 'compilation', 'supplementaire', 'nomme', 'manner', 'songs', 'cooperative', 'pathways', 'minako', 'ciblee', 'simple', 'plotlinesthe', 'principally', 'branch', 'trop', 'alter', 'tecmo', 'gamestop', 'arme', 'japonen', 'lacs', 'becomes', 'giving', 'rockstars', 'pirates', 'annees', 'climats', 'celebrate', 'puzzle', 'possible', 'flashbackquete', 'translator', 'observation', 'dream', 'nouvelle', 'international', 'mondes', 'rerelease', 'sound', 'avec', 'montagnard', 'desire', 'epic', 'about', 'enfants', 'short', 'mettre', 'douvrir', 'gametrailers', 'number', 'seeing', 'fonctionnalites', 'showcased', 'global', 'editee', 'lost', 'childhood', 'empirehouser', 'compressed', 'deroule', 'liberte', 'plusieurs', 'racetrack', 'declin', 'gamer', 'awards', 'promenades', 'involved', 'dautres', 'sauvegarde', 'lock', 'beyond', 'evenements', 'facultative', 'early', 'fois', 'bestiale', 'lemplacement', 'delayed', 'vigil', 'making', 'doreesles', 'coworkers', 'australiathe', 'suit', 'nintendoannees', 'cooperation', 'installments', 'revient', 'began', 'consisted', 'facteurs', 'interviews', 'dires', 'celebre', 'collectively', 'york', 'hunt', 'dutiliser', 'compromise', 'levelbased', 'capacite', 'scoresas', 'orne', 'representatifs', 'care', 'encapuchonnees', 'members', 'extremement', 'lorigine', 'filet', 'imprisoning', 'horseback', 'medieval', 'wagners', 'dessin', 'seul', 'vraiment', 'items', 'pitch', 'parallelevictoire', 'arguably', 'reste', 'snes', 'similar', 'histoire', 'devoilant', 'body', 'communaute', 'venue', 'melangeant', 'voeu', 'colossus', 'flots', 'sheik', 'miniiles', 'echanges', 'prend', 'miyamoto', 'collectorsune', 'shrunk', 'acorn', 'mitigees', 'skulltulas', 'direct', 'licence', 'plus', 'sharpened', 'enfant', 'lemarchand', 'daemon', 'critiquee', 'durant', 'shout', 'highly', 'players', 'gladiators', 'vogel', 'writer', 'vowed', 'skyward', 'dessous', 'redmond', 'forests', 'evolue', 'ganonthe', 'sheikahs', 'ambiance', 'among', 'conference', 'achieve', 'resolution', 'musique', 'francis', 'goldcoloured', 'layout', 'gallinace', 'telecommande', 'serieun', 'scholastic', 'novels', 'data', 'lequel', 'accorde', 'adulteganon', 'tente', 'overworld', 'intermission', 'could', 'terrifiante', 'righteous', 'returned', 'miyazaki', 'definie', 'autres', 'exclusivement', 'rereleased', 'into', 'espace', 'reach', 'midjune', 'styles', 'quinze', 'france', 'creaturesthe', 'develop', 'philips', 'systems', 'tournee', 'desert', 'official', 'comportant', 'sortie', 'zeldail', 'descends', 'developers', 'dorefah', 'barton', 'loccasionle', 'legends', 'parcourant', 'devenements', 'atari', 'presence', 'officiel', 'highdefinition', 'insectes', 'skimos', 'omen', 'colin', 'preordered', 'brosin', 'apprehensively', 'epoch', 'source', 'caves', 'real', 'approaches', 'ethereal', 'taille', 'pure', 'puissent', 'mirabella', 'gannon', 'detail', 'personnage', 'dapparaitre', 'trompette', 'surface', 'extension', 'listshowplatform', 'paradoxe', 'copyright', 'alliance', 'coeurs', 'ajoutes', 'bonus', 'increased', 'program', 'plot', 'treize', 'lack', 'englouti', 'destroyed', 'origins', 'talked', 'zeldas', 'inedites', 'justin', 'preapocalyptique', 'ajout', 'human', 'exclude', 'obligeant', 'obtenu', 'fait', 'deffets', 'innovations', 'race', 'empire', 'ajoute', 'lhistoire', 'impending', 'etre', 'instruction', 'standards', 'learn', 'amicalesquetes', 'rage', 'oiseau', 'arrows', 'titled', 'size', 'amene', 'conceived', 'soundtrack', 'quelques', 'connue', 'rogers', 'info', 'cities', 'vient', 'calvert', 'mario', 'actions', 'singleplayer', 'awakening', 'mechanic', 'versions', 'tenebres', 'montagne', 'temporel', 'console', 'expanded', 'mahardy', 'helpful', 'compose', 'concert', 'august', 'scattered', 'commercialisee', 'loresouls', 'gameplay', 'expired', 'retaining', 'active', 'tasked', 'rearranges', 'amelioration', 'future', 'inishie', 'boussole', 'translates', 'child', 'plupart', 'symphonic', 'andrew', 'nindb', 'network', 'used', 'deesses', 'tard', 'getting', 'dataforlag', 'bestselling', 'dores', 'majority', 'assume', 'donnant', 'ennemis', 'loccasion', 'registering', 'beloved', 'suffers', 'full', 'tells', 'hyrule', 'attempt', 'gamelon', 'varying', 'jouees', 'overview', 'partially', 'jeune', 'situant', 'cganimated', 'twilis', 'dynasty', 'koholint', 'fails', 'normal', 'california', 'haut', 'existent', 'developpeurs', 'talk', 'healththe', 'spot', 'occidentale', 'never', 'clairement', 'bellthe', 'dobjets', 'maintenant', 'mort', 'pointues', 'aquatiques', 'lessentiel', 'entered', 'leur', 'lorsquils', 'paying', 'west', 'certaines', 'filmworks', 'importante', 'david', 'facon', 'lyre', 'square', 'enters', 'faits', 'alimente', 'april', 'materials', 'receive', 'sest', 'niveaux', 'impacted', 'leau', 'predecesseurs', 'peripheral', 'telle', 'washington', 'donjons', 'siliconera', 'dimension', 'longtemps', 'zelda', 'including', 'lechange', 'ataru', 'license', 'quete', 'neal', 'most', 'fire', 'jardin', 'primordial', 'target', 'stupides', 'majora', 'emplis', 'ever', 'role', 'musicinspirationthe', 'machines', 'contre', 'includes', 'major', 'mark', 'difficulte', 'controlable', 'motives', 'mermusiquecette', 'vendue', 'embranchement', 'section', 'zeldalune', 'batterybacked', 'themes', 'faces', 'eponymous', 'failed', 'gamerankings', 'darknut', 'sounds', 'germany', 'kept', 'livrecrypte', 'highfantasy', 'voiceacted', 'pushpull', 'peace', 'dscrossoversthe', 'door', 'timethe', 'grosse', 'paralleles', 'regenerent', 'stop', 'wikipedia', 'rapide', 'etant', 'lexistence', 'todays', 'following', 'timeles', 'mature', 'converti', 'lineaire', 'litterature', 'laventure', 'publications', 'ventured', 'possess', 'gottliebs', 'played', 'mediavaliant', 'suivie', 'mention', 'consoles', 'entierement', 'laide', 'ailes', 'unique', 'dualscreen', 'highest', 'kokiris', 'novelist', 'secondaires', 'bonheur', 'semblait', 'every', 'controlling', 'soigner', 'wild', 'dorchestre', 'nimporte', 'heuristic', 'nayru', 'loses', 'arriver', 'exaucant', 'citing', 'animation', 'bibliographie', 'designer', 'pastnintendo', 'obtenir', 'uses', 'home', 'what', 'material', 'martin', 'parmi', 'clue', 'shall', 'lutte', 'lere', 'experimented', 'cloud', 'block', 'telechargement', 'retient', 'heart', 'shields', 'their', 'japanese', 'life', 'pointyeared', 'succes', 'convenableainsi', 'united', 'reflect', 'themed', 'chapter', 'coincide', 'celestia', 'mentioned', 'thoughts', 'gamesmain', 'cultivated', 'lives', 'meilleur', 'mogmas', 'timelimit', 'plan', 'gamesthroughout', 'century', 'laveu', 'plumes', 'cocorico', 'realistically', 'dsiware', 'princessfin', 'marines', 'musiquele', 'routes', 'loyalty', 'significant', 'motif', 'licensing', 'look', 'prominent', 'disparu', 'ingame', 'editors', 'competences', 'dailleurs', 'seasonsthe', 'garos', 'inclus', 'accepts', 'acceder', 'dooming', 'cotes', 'nommee', 'zeldale', 'meant', 'regular', 'enigme', 'purorogu', 'mielke', 'millions', 'remainocarina', 'rich', 'tels', 'semblables', 'contextsensitive', 'sonic', 'conserver', 'americaine', 'ones', 'edge', 'porting', 'utilisation', 'chateau', 'tester', 'website', 'unknown', 'award', 'legacy', 'tracey', 'appele', 'oregon', 'remake', 'connexe', 'egms', 'ensemble', 'order', 'joueren', 'bongos', 'personnages', 'chronology', 'reincarnation', 'discounted', 'decline', 'floating', 'commissioned', 'derivee', 'suellentrop', 'september', 'stealth', 'redevenu', 'melta', 'strength', 'brows', 'cavernes', 'complet', 'disembodied', 'triforce', 'malefique', 'livre', 'japonais', 'jouable', 'powerful', 'hope', 'ending', 'gardant', 'siecle', 'tournait', 'brett', 'manifests', 'colore', 'netait', 'album', 'episodesref', 'urbosa', 'amount', 'darunia', 'disambiguationloz', 'tingle', 'reveals', 'chronologies', 'simultanement', 'necessaire', 'descended', 'bros', 'says', 'genres', 'traversee', 'scene', 'episode', 'predominantly', 'ravel', 'paraduses', 'classic', 'creator', 'quality', 'franchises', 'petit', 'oriente', 'keys', 'japaneseonly', 'empechermangasune', 'topdown', 'responsesprincess', 'adaptations', 'tale', 'implicitly', 'advance', 'commence', 'chronologiquement', 'incarnations', 'jamess', 'classer', 'wiiannees', 'vingtcinq', 'plans', 'subject', 'titrant', 'chests', 'rejected', 'originale', 'vigilant', 'sortis', 'eiji', 'symphonie', 'dhyrule', 'phases', 'makuch', 'piano', 'elements', 'revelent', 'starting', 'franchiseafter', 'stylet', 'improve', 'exemple', 'crossovers', 'telling', 'north', 'bomb', 'pierres', 'celestiens', 'pasts', 'heroes', 'gamespy', 'souls', 'gave', 'quitter', 'world', 'similarities', 'swedish', 'referred', 'tete', 'along', 'cinq', 'voient', 'animearticle', 'granted', 'excepte', 'weapons', 'serieslinkmain', 'recompense', 'optimise', 'musictaking', 'variees', 'added', 'commun', 'arbre', 'multiple', 'permettent', 'battler', 'compositeur', 'airing', 'zeldanintendo', 'initially', 'akira', 'lieux', 'modifiee', 'medstroms', 'kennedy', 'twili', 'moindres', 'requiring', 'invisible', 'touche', 'printer', 'plots', 'adaption', 'antre', 'than', 'interactivity', 'dehors', 'company', 'ressemblent', 'revali', 'locked', 'pioneered', 'dune', 'discovery', 'joystiqcombrandon', 'adventurebattle', 'majoras', 'crossover', 'gives', 'deverrouiller', 'challenged', 'villain', 'existence', 'werent', 'four', 'bannies', 'fares', 'vetus', 'transformes', 'bows', 'pleasant', 'large', 'linked', 'exchanged', 'poeme', 'ranked', 'atmosphere', 'jose', 'away', 'merous', 'developpes', 'pose', 'already', 'donc', 'contemporary', 'namcos', 'dash', 'mont', 'additions', 'yells', 'pelland', 'barriere', 'tael', 'etres', 'volcanique', 'believes', 'producing', 'depicted', 'reedition', 'temporelle', 'secondhand', 'past', 'shorts', 'debloquer', 'guere', 'bombs', 'vision', 'gamebooks', 'chief', 'antagonist', 'show', 'portable', 'renvoie', 'laquelle', 'tutelle', 'depths', 'precieuses', 'posits', 'accomplish', 'shoemaker', 'lembleme', 'dedie', 'norris', 'minuscule', 'medias', 'ralliees', 'outsourced', 'fall', 'rencontrer', 'boomerangs', 'lumiere', 'dactionaventure', 'guide', 'greatest', 'sinspire', 'diffusion', 'jument', 'heros', 'opportunity', 'young', 'ayant', 'chart', 'unsourced', 'persistant', 'possibilite', 'figurine', 'octorocks', 'magical', 'download', 'radicalementthe', 'return', 'heavy', 'situated', 'amazoncom', 'fouille', 'mecanique', 'whole', 'navire', 'seconde', 'additional', 'enfanceprotection', 'artifacts', 'creed', 'newswire', 'hamano', 'seriesin', 'textures', 'zones', 'parer', 'aquatique', 'frame', 'residant', 'ocean', 'demon', 'figures', 'cree', 'chaque', 'fred', 'conteneur', 'explorations', 'strategic', 'differentes', 'mcwhertor', 'cagiva', 'tradition', 'lennemi', 'hyliens', 'saria', 'principaleimage', 'solo', 'effets', 'then', 'templesthe', 'alters', 'designed', 'periodically', 'possede', 'were', 'avril', 'affected', 'loriginalite', 'conferencelane', 'army', 'actually', 'coeur', 'freshlypicked', 'loosely', 'separate', 'specifique', 'pichlmair', 'monde', 'labyrinthes', 'warn', 'million', 'lexception', 'midi', 'dilesthe', 'claimed', 'device', 'sangliers', 'thought', 'primarily', 'certaine', 'ciela', 'batterie', 'completeness', 'share', 'balanced', 'general', 'shades', 'presents', 'episodes', 'power', 'franchissement', 'ishinomori', 'leading', 'subtitle', 'miyamotos', 'forts', 'messagemain', 'memorables', 'setting', 'rassemble', 'published', 'worthy', 'battles', 'page', 'hearts', 'incitation', 'forcenintendo', 'reflects', 'heads', 'winds', 'amazons', 'principal', 'reveal', 'cercueil', 'grandes', 'bring', 'demise', 'forbes', 'minijeux', 'poem', 'pieces', 'degree', 'indiscriminately', 'warp', 'left', 'accompagnee', 'milwaukie', 'habituelles', 'states', 'timecharacterssee', 'referenced', 'feature', 'shadow', 'lezard', 'offputting', 'boar', 'completely', 'allow', 'minute', 'marge', 'appears', 'utilite', 'presenter', 'annonce', 'gains', 'suffered', 'timemax', 'edition', 'printera', 'pages', 'celtique', 'perd', 'accrue', 'rise', 'puzzlebased', 'doiseaux', 'release', 'timeline', 'lors', 'peuples', 'hacheviande', 'resurrection', 'norrispinballcom', 'mondiale', 'controllable', 'molyneuxs', 'multijoueur', 'protagonists', 'something', 'best', 'reading', 'president', 'shortly', 'sujet', 'musicmaking', 'malediction', 'caverne', 'family', 'dialogue', 'combat', 'termina', 'sidon', 'destroy', 'wwwnintendocom', 'spirits', 'volcan', 'dabord', 'musiques', 'raison', 'minor', 'proceedings', 'march', 'emulated', 'campagnards', 'transition', 'wander', 'totalement', 'considerent', 'stay', 'forms', 'circuit', 'ceuxla', 'endroit', 'engine', 'magie', 'optimised', 'consistent', 'exposed', 'please', 'adding', 'manque', 'swordsthe', 'devoilees', 'replenish', 'laction', 'supervision', 'public', 'seraient', 'modification', 'individual', 'this', 'famille', 'find', 'pressing', 'screen', 'populations', 'locations', 'playersbreath', 'adapted', 'opus', 'dadopter', 'legacyaggregate', 'fable', 'sont', 'metroid', 'threats', 'statues', 'software', 'mystical', 'movies', 'detablir', 'humanity', 'adulthood', 'fighting', 'transportation', 'retains', 'humanoids', 'techradar', 'reperer', 'given', 'remaining', 'kingdom', 'effet', 'medolie', 'shooter', 'lakes', 'nindoricom', 'controler', 'graphical', 'continues', 'media', 'over', 'dexploration', 'deuxieme', 'sekiban', 'liberer', 'throughout', 'denlever', 'gerudos', 'green', 'vice', 'houser', 'ravels', 'relying', 'pokemon', 'milieux', 'petite', 'change', 'felonious', 'creating', 'sharon', 'climb', 'miniature', 'clef', 'base', 'difficultes', 'predestined', 'agahnim', 'nonjoueurs', 'followed', 'gained', 'especes', 'remakes', 'basant', 'interactive', 'sibyllin', 'pere', 'cible', 'debloque', 'wisdom', 'simply', 'make', 'bundled', 'techniques', 'daccomplir', 'ameliorant', 'received', 'prevue', 'spear', 'phil', 'picking', 'astro', 'february', 'xvother', 'habitaient', 'lhyrule', 'decided', 'working', 'dual', 'difficult', 'island', 'nouveaux', 'heroto', 'defeats', 'brian', 'tree', 'vejvoda', 'secretes', 'simplified', 'connu', 'triforcemis', 'these', 'them', 'oeuvre', 'toujours', 'placement', 'indicates', 'collectors', 'modified', 'didnt', 'lorule', 'cancelled', 'down', 'consumed', 'paradisenintendo', 'retrouve', 'total', 'amazon', 'pointed', 'include', 'deroulent', 'dated', 'protagonist', 'cartouches', 'zeldaan', 'retarder', 'diverses', 'totaka', 'darmani', 'principaleannees', 'uniques', 'garcon', 'scripted', 'kamiya', 'forming', 'dernier', 'balloon', 'witcher', 'matt', 'imagine', 'reprises', 'dobtenir', 'storytelling', 'kart', 'same', 'principalla', 'enemies', 'celui', 'features', 'sealed', 'gamescdi', 'refonte', 'timein', 'aonuma', 'royaumele', 'aussi', 'secraser', 'chaos', 'trouver', 'carquois', 'fourni', 'whose', 'scenario', 'secluded', 'reserver', 'beaten', 'adams', 'protecteurs', 'rare', 'formnintendo', 'quant', 'uphold', 'controle', 'between', 'lutilisation', 'open', 'dauteur', 'entrances', 'parallel', 'work', 'companies', 'kingdomthe', 'scaff', 'dreams', 'videogames', 'older', 'critics', 'differe', 'heavily', 'currently', 'late', 'vide', 'verte', 'poiscoms', 'propose', 'sacred', 'table', 'solid', 'allows', 'pattes', 'inconnu', 'laccueillir', 'penser', 'reception', 'remove', 'fight', 'portuguese', 'styled', 'mysterious', 'specific', 'peter', 'hatfield', 'remains', 'interpreted', 'party', 'countdown', 'swordjose', 'mute', 'itoi', 'series', 'fantasy', 'written', 'constant', 'takes', 'precedes', 'play', 'enfin', 'cris', 'outside', 'wiis', 'okami', 'whether', 'minimalist', 'bombe', 'zeldaen', 'utilisant', 'passent', 'inconsistencies', 'touffe', 'chemin', 'bookszelda', 'jupiter', 'navaient', 'second', 'scission', 'like', 'confidential', 'grey', 'backstory', 'subscription', 'sources', 'launch', 'neededin', 'receptacles', 'defeating', 'redirects', 'that', 'voyage', 'defeated', 'judge', 'meme', 'wiimotion', 'predecesseur', 'oceans', 'fairies', 'bosses', 'unlike', 'railroads', 'expirea', 'entrance', 'darksiders', 'actionorientedwhen', 'magician', 'votre', 'november', 'raconte', 'morceau', 'reel', 'realtime', 'cartridgessfour', 'recuperer', 'enlightenment', 'parsemes', 'worst', 'ricardo', 'paralyser', 'apparu', 'appreciee', 'provient', 'voleuses', 'brawl', 'woods', 'dont', 'disponible', 'wing', 'unostyled', 'constants', 'propre', 'baptisee', 'october', 'zeldazelda', 'became', 'localizing', 'secondesdurant', 'sommaire', 'cover', 'ganon', 'reborn', 'koeis', 'trouvera', 'onto', 'obtenue', 'choice', 'cave', 'forets', 'princesses', 'limited', 'feel', 'palais', 'origin', 'zeldasysteme', 'moblins', 'gamefaqs', 'gmbh', 'fame', 'territoire', 'souterrains', 'compte', 'zeldathemed', 'nexiste', 'oreilles', 'visible', 'live', 'troquer', 'name', 'leaps', 'parseme', 'sagissait', 'couleur', 'later', 'integralement', 'critically', 'scheduled', 'puissante', 'fulfilled', 'ganondorfs', 'devoile', 'passe', 'standalone', 'devie', 'vert', 'permet', 'oldest', 'reviewers', 'check', 'revealed', 'player', 'racing', 'minuscules', 'ziff', 'still', 'japonaise', 'voit', 'kingdomdengeki', 'dechapper', 'mostly', 'eddie', 'novembre', 'seek', 'deternels', 'launches', 'incomplete', 'recurring', 'colorbased', 'puis', 'ventes', 'rubis', 'fact', 'suspension', 'korean', 'questsin', 'press', 'catalogue', 'having', 'tassi', 'cdrom', 'significantly', 'commemorate', 'purchases', 'developpementau', 'colores', 'interact', 'those', 'commande', 'suivant', 'idea', 'text', 'monstrous', 'denigmes', 'accessible', 'triforcereeditions', 'primitive', 'virtuelle', 'organisee', 'first', 'parce', 'masques', 'walt', 'habitent', 'changement', 'transformer', 'massive', 'named', 'story', 'gold', 'donnent', 'missionnintendo', 'limage', 'reduced', 'demo', 'grab', 'animee', 'crunchyroll', 'reedites', 'videogame', 'shogakukan', 'etabli', 'ceux', 'containers', 'amerique', 'ligne', 'alors', 'vary', 'extra', 'organise', 'sybex', 'hobo', 'promotion', 'upcoming', 'zach', 'kain', 'quatre', 'largement', 'handheld', 'enjoyed', 'your', 'verrouille', 'sagesneil', 'invades', 'mangas', 'inexistants', 'makes', 'design', 'apparaissant', 'ressusciter', 'cartoon', 'ported', 'supplementaires', 'apparaissent', 'more', 'broadcast', 'combataudiokoji', 'memorable', 'passage', 'visage', 'timelong', 'kohler', 'souvenir', 'production', 'hylia', 'videoles', 'multidirectional', 'controller', 'seuls', 'quickly', 'coordinating', 'truly', 'latest', 'saga', 'battre', 'cited', 'spirit', 'card', 'yunobo', 'passee', 'strong', 'vaati', 'sleeping', 'daniel', 'potential', 'ouvert', 'essentiellement', 'semblable', 'perfect', 'kondoplatforms', 'proved', 'expansion', 'result', 'believing', 'average', 'protegee', 'established', 'club', 'camera', 'payants', 'egalement', 'silent', 'together', 'marksmanship', 'begins', 'setendant', 'bienvenue', 'paralleledefaite', 'avait', 'rend', 'guardians', 'soupe', 'titles', 'securing', 'iasig', 'hormis', 'audessus', 'thousands', 'skull', 'bras', 'core', 'contained', 'amicales', 'middle', 'escaping', 'ladaptation', 'faisant', 'decouvrir', 'near', 'cartes', 'importantes', 'manager', 'credithugh', 'officiellement', 'objets', 'melange', 'aided', 'exemplaires', 'ledification', 'metacriticthe', 'nintendocom', 'campagne', 'studio', 'phare', 'dernieres', 'eight', 'speaks', 'labrynna', 'dordinn', 'eoliens', 'grottes', 'contient', 'suggera', 'temples', 'intelligents', 'want', 'finalement', 'friday', 'locarina', 'western', 'ability', 'riju', 'limitations', 'divers', 'bateau', 'complete', 'sidescrolling', 'compagnons', 'information', 'dragon', 'been', 'scoring', 'remastering', 'departing', 'autrement', 'pris', 'npcs', 'environmental', 'villagesmais', 'today', 'chose', 'humanoide', 'tourne', 'jeuarticle', 'tetra', 'mowatt', 'manier', 'loup', 'chef', 'limitees', 'detaille', 'timelines', 'half', 'varied', 'start', 'leitmotifs', 'ways', 'expressed', 'jack', 'resting', 'noting', 'issus', 'vend', 'toki', 'hors', 'contes', 'settings', 'utilisee', 'addition', 'occur', 'papillons', 'taller', 'poor', 'interview', 'trendsmcwhertor', 'inspired', 'termes', 'mediaworks', 'movement', 'commercialserie', 'emphasize', 'hidetaka', 'instead', 'brigands', 'ereadercancelled', 'template', 'suivants', 'combattent', 'rumeur', 'empli', 'miroir', 'theft', 'temps', 'multiplayer', 'ambulants', 'individuals', 'gottlieb', 'murmured', 'from', 'tezukacomposers', 'ambience', 'nouveau', 'font', 'convergence', 'generalement', 'graphics', 'kayas', 'laccessoire', 'kara', 'cocottes', 'ashcraft', 'realmin', 'doreenintendo', 'caracterisees', 'envahit', 'voir', 'saint', 'hidden', 'commonly', 'developed', 'boat', 'disneys', 'carte', 'enemiesthe', 'abandonne', 'explored', 'acquis', 'dreamfictional', 'portion', 'gamesradar', 'mythology', 'known', 'voix', 'performances', 'celshading', 'gamecube', 'rendent', 'hajime', 'dans', 'cartridge', 'hideki', 'password', 'lovely', 'mianimale', 'collection', 'warping', 'ecrit', 'dixneuf', 'jamais', 'barcode', 'flagship', 'according', 'mythologiques', 'minimal', 'kidnapping', 'digra', 'list', 'hundred', 'reverse', 'anthropomorphic', 'divinity', 'nakatsuka', 'continued', 'proposer', 'perhaps', 'steeped', 'site', 'domination', 'zapper', 'shows', 'sort', 'coups', 'product', 'vingt', 'said', 'kind', 'differente', 'contrepartie', 'interacting', 'doivent', 'report', 'grant', 'crypte', 'executive', 'modifications', 'ruines', 'labyrinthine', 'densetsu', 'realisee', 'dessus', 'mauvaise', 'winfried', 'followup', 'seal', 'outre', 'actual', 'americanotes', 'offert', 'goddess', 'cracheurs', 'demonstration', 'kill', 'clarified', 'right', 'lanterne', 'smash', 'decembre', 'lien', 'prince', 'princessen', 'devinrent', 'which', 'princesse', 'qualite', 'gameepisode', 'tokays', 'disappearing', 'consideree', 'clefs', 'essaye', 'celesbourg', 'repaire', 'napparait', 'much', 'linstant', 'blood', 'view', 'foret', 'rearranged', 'rapidement', 'fourth', 'incluent', 'help', 'triforces', 'parallele', 'passed', 'croit', 'dorees', 'slashstyle', 'cardscanning', 'popularity', 'centres', 'stone', 'deku', 'liens', 'abilities', 'lecteur', 'replenished', 'sands', 'arriere', 'forever', 'peche', 'trouves', 'spaceworld', 'regroupant', 'collaborations', 'augmente', 'american', 'transformee', 'craig', 'sils', 'entier', 'studios', 'insuffisamment', 'gagner', 'lopus', 'capacites', 'commander', 'customers', 'using', 'gamerscom', 'nourriture', 'wide', 'timenintendo', 'deviendra', 'tragedy', 'digital', 'magique', 'vendus', 'raccourcis', 'supercontinent', 'officielle', 'picross', 'magic', 'assez', 'comes', 'dire', 'nearly', 'hyliennes', 'depuis', 'person', 'taya', 'accompagne', 'openingsa', 'incarnation', 'essays', 'formant', 'toute', 'went', 'recurrents', 'memes', 'movie', 'gamepad', 'animaux', 'compares', 'swordin', 'acknowledged', 'lands', 'principaux', 'instance', 'status', 'whereas', 'extend', 'completement', 'satellaviews', 'grands', 'gerudo', 'offjonti', 'suggestion', 'navigating', 'youth', 'reprenant', 'annexe', 'taking', 'websites', 'conduisant', 'rockstar', 'reunite', 'independants', 'comprising', 'genre', 'aggregator', 'column', 'mais', 'fragments', 'passwords', 'rares', 'contrat', 'springs', 'pour', 'dikana', 'producer', 'needed', 'prior', 'deroules', 'embodies', 'allplunkett', 'secret', 'hints', 'took', 'listed', 'rankings', 'tuer', 'melodies', 'derniere', 'exceptions', 'although', 'mihommes', 'surprise', 'revela', 'simultaneously', 'mojo', 'setant', 'travail', 'iria', 'elle', 'relique', 'clear', 'archived', 'mipha', 'came', 'ultimate', 'review', 'dexemplaires', 'chevauchent', 'encore', 'even', 'dautre', 'mauvais', 'technology', 'bookta', 'tests', 'davis', 'such', 'decouverte', 'mots', 'zerudanochuanshuo', 'scaled', 'does', 'citizen', 'grezzopublishers', 'farore', 'jawdropping', 'maniere', 'communs', 'navi', 'disambiguationthe', 'vitality', 'ornee', 'vaste', 'screwattacks', 'chain', 'europeen', 'altered', 'deblaye', 'reviews', 'maximale', 'mitch', 'nearby', 'langley', 'highestrated', 'resolu', 'theme', 'dispose', 'speculated', 'whitehead', 'article', 'periode', 'foreground', 'worlds', 'artwork', 'versa', 'morceaux', 'confirme', 'heartthe', 'antagonists', 'audela', 'years', 'hardware', 'sept', 'nouvelles', 'grappin', 'gamesthe', 'through', 'experiences', 'tommy', 'quelquesuns', 'historique', 'types', 'progressing', 'femelles', 'tmnt', 'special', 'dessine', 'modes', 'totalite', 'seriesthree', 'goodfellas', 'peuplent', 'publishing', 'another', 'essentiel', 'important', 'echoue', 'zeldaaccording', 'generation', 'yuichi', 'concepteurs', 'hylian', 'travel', 'melee', 'maurice', 'remote', 'stricte', 'eaux', 'next', 'moderne', 'fini', 'graphismes', 'color', 'implique', 'serieshearing', 'unnamed', 'informer', 'orchestra', 'retail', 'difficiles', 'elles', 'outstanding', 'masque', 'cent', 'chevaliers', 'profil', 'month', 'notamment', 'minimum', 'timecest', 'inspiration', 'remnants', 'principalement', 'servir', 'ganondorf', 'takizawa', 'contains', 'apparait', 'controlled', 'telechargeable', 'cours', 'arcade', 'backstories', 'dassener', 'changer', 'physically', 'parties', 'expansive', 'prevu', 'prequelle', 'exploree', 'kyoto', 'particularites', 'visant', 'instruments', 'stories', 'current', 'deviennent', 'points', 'cancel', 'culture', 'tribute', 'adventures', 'potion', 'chronicles', 'monture', 'principles', 'proposes', 'hesite', 'showing', 'cependant', 'accueil', 'armes', 'guitare', 'have', 'conception', 'dstyled', 'premier', 'thirst', 'ledition', 'jeule', 'well', 'citations', 'americain', 'previous', 'fantastique', 'rapprochant', 'handicapant', 'siecles', 'concept', 'creation', 'tunic', 'refinements', 'needing', 'cartridges', 'uncharted', 'dunites', 'informations', 'roberts', 'bloodline', 'consolesocarina', 'encyclopediathis', 'wilds', 'taupes', 'gamespot', 'marpo', 'legend', 'landsettingmain', 'lacoste', 'aventure', 'knight', 'precedent', 'death', 'nouvel', 'combining', 'welsh', 'revele', 'successful', 'called', 'people', 'vendues', 'association', 'wear', 'dexcellents', 'flaming', 'vaincu', 'toutefois', 'magazine', 'released', 'reedite', 'both', 'film', 'editions', 'exposition', 'further', 'explorer', 'couleurs', 'panlink', 'trailer', 'fast', 'michael', 'dhyrulearticle', 'except', 'apparaitre', 'polygon', 'connected', 'desktops', 'continuation', 'facteur', 'guinness', 'utilise', 'teleporteurs', 'master', 'gamesat', 'nothing', 'trap', 'everimpactmultiple', 'contain', 'runes', 'subrosia', 'musical', 'lawshigeru', 'disque', 'fantomatiques', 'okamoto', 'progress', 'video', 'limite', 'descendance', 'quests', 'speaking', 'porter', 'koji', 'penetrer', 'diverted', 'annoncerent', 'pestes', 'vent', 'japon', 'acces', 'quun', 'letre', 'introduced', 'wildmarch', 'offer', 'legendary', 'each', 'saisons', 'righthanded', 'titre', 'towns', 'premiere', 'will', 'orchestrated', 'however', 'tous', 'composition', 'represented', 'environnement', 'black', 'exclusively', 'captain', 'hysteria', 'recorder', 'announcement', 'restored', 'connecting', 'accepted', 'defait', 'larme', 'resoudre', 'bourse', 'invertebres', 'lorsquil', 'coming', 'foretoldshigeru', 'commercial', 'concerts', 'seasons', 'exclusives', 'fevrier', 'crossbow', 'fate', 'attack', 'told', 'vaincre', 'precision', 'tetras', 'universe', 'aliases', 'enabling', 'leader', 'emparer', 'village', 'suivantes', 'week', 'aspects', 'training', 'pack', 'sonores', 'experience', 'succeed', 'teased', 'because', 'soixantedouze', 'swordlors', 'progresses', 'infamous', 'jour', 'dates', 'islandfilled', 'rouge', 'appeles', 'enfancele', 'lead', 'shop', 'curse', 'zeruda', 'oppose', 'troisieme', 'doorways', 'enough', 'comfortable', 'shinbun', 'personnes', 'differents', 'retranscrits', 'dadresse', 'ganonplus', 'print', 'flows', 'reelle', 'inhabitants', 'microsoft', 'brilliant', 'arise', 'fran', 'gods', 'mythologie', 'relative', 'either', 'flag', 'enigmes', 'function', 'wakerthe', 'gorons', 'lapparence', 'crepuscule', 'designing', 'villages', 'sounded', 'answer', 'tell', 'seigneur', 'chronologie', 'planning', 'splits', 'contrairement', 'characters', 'appris', 'presente', 'america', 'enacted', 'chacun', 'confirma', 'audience', 'connut', 'debut', 'mivegetale', 'apparus', 'example', 'lumineuse', 'disagreed', 'proceeding', 'contents', 'also', 'become', 'stated', 'himself', 'chasseurs', 'debate', 'lifespan', 'earth', 'hyrulian', 'possedees', 'limportance', 'fictional', 'downloadable', 'integrated', 'found', 'boomerang', 'foule', 'question', 'arms', 'revanche', 'wont', 'monopoly', 'restore', 'july', 'principale', 'piafs', 'zeldafebruary', 'soul', 'confirmed', 'puisque', 'taquinees', 'oracle', 'within', 'obtain', 'ages', 'milodon', 'joueurs', 'employee', 'particularly', 'fitzgeraldganonmain', 'apres', 'virtual', 'neil', 'boite', 'means', 'gamepro', 'angeles', 'some', 'zeldafrom', 'bolero', 'entirely', 'takashi', 'female', 'novel', 'inchange', 'protection', 'battling', 'paul', 'wish', 'tracksin', 'staff', 'baba', 'larbre', 'independently', 'nest', 'slowly', 'evolutions', 'laterreleased', 'particulier', 'narratif', 'deviation', 'creusant', 'guides', 'essayant', 'blobs', 'parodies', 'hero', 'objectives', 'popfiction', 'single', 'categories', 'annoncee', 'seasonprint', 'choppier', 'symphony', 'precommande', 'exelo', 'roleplaying', 'better', 'nintendos', 'ocarina', 'ends', 'aide', 'ranks', 'limitee', 'moon', 'part', 'elfes', 'line', 'famicom', 'surrounding', 'knitted', 'toon', 'certains', 'perspective', 'egos', 'donjonsarticle', 'heartbased', 'subsequent', 'different', 'triangles', 'disc', 'trois', 'produced', 'linking', 'star', 'dherbe', 'numerises', 'divinites', 'completing', 'liveaction', 'retrouver', 'quelque', 'cranes', 'accordait', 'cela', 'inside', 'rural', 'animated', 'lindustrie', 'explorereception', 'lage', 'locating', 'ocarinas', 'rennes', 'merely', 'favorite', 'projekt', 'reality', 'serve', 'ztargeting', 'serieconsole', 'sequels', 'conjunction', 'dynamics', 'link', 'joues', 'exception', 'central', 'emblem', 'episodespendant', 'directement', 'ainsi', 'royal', 'enfance', 'content', 'serieslcd', 'repurpose', 'marque', 'epona', 'linterieur', 'logique', 'vivant', 'rupee', 'prophecy', 'gaiden', 'josh', 'derouler', 'tour', 'spirituel', 'confondre', 'daruk', 'vaincus', 'difference', 'kodai', 'rang', 'puzzlesolving', 'take', 'firone', 'supporting', 'describing', 'fumito', 'theyve', 'tout', 'tikwis', 'vendu', 'reliee', 'featured', 'employed', 'steal', 'impressions', 'contexts', 'becensabot', 'mediatv', 'segment', 'skyloft', 'bundle', 'holodrum', 'lantern', 'captured', 'thereafter', 'announces', 'lunivers', 'retour', 'withstand', 'placing', 'sweden', 'soleil', 'widespread', 'viacom', 'glenn', 'vivent', 'recordsle', 'coffres', 'magasin', 'walton', 'immortal', 'moteur', 'morts', 'princess', 'candleocarina', 'signe', 'scullion', 'sonobe', 'hesitation', 'tracksthe', 'peuvent', 'atteindre', 'tabata', 'crackedcomnorris', 'semaines', 'warrior', 'trame', 'wessel', 'darkness', 'creees', 'laerouage', 'mesure', 'representes', 'chronologiea', 'readied', 'ganons', 'villains', 'sous', 'present', 'thing', 'artifact', 'document', 'books', 'quetes', 'jusqua', 'terre', 'intitule', 'derivesdessin', 'meets', 'esprits', 'sets', 'placed', 'molyneux', 'departure', 'fromsoftware', 'forced', 'tezuka', 'centers', 'hourglass', 'accessibles', 'june', 'might', 'motionplus', 'developper', 'permettraient', 'particularite', 'arthurian', 'spinoff', 'mechanics', 'avaient', 'sold', 'quil', 'monstres', 'puzzles', 'seen', 'gamecubecitation', 'year', 'needs', 'ozaki', 'cite', 'leurs', 'division', 'while', 'queue', 'must', 'etaient', 'rooms', 'insere', 'reversed', 'aujourdhui', 'adulte', 'events', 'premiers', 'lepee', 'plaine', 'failure', 'offre', 'grezzo', 'aggregate', 'hillsides', 'utiliser', 'smaller', 'sorte', 'differently', 'offered', 'combats', 'cycle', 'americana', 'able', 'overarching', 'unlock', 'memory', 'habite', 'sequel', 'lediteur', 'approach', 'being', 'proche', 'online', 'profite', 'monsters', 'nikkan', 'obtained', 'toymax', 'straightforward', 'expanding', 'himekawa', 'tingles', 'kazumi', 'element', 'semparer', 'directe', 'lile', 'shield', 'provided', 'created', 'extensive', 'comics', 'farted', 'precedents', 'lars', 'excalibur', 'tient', 'soit', 'cocolint', 'animal', 'exploration', 'everything', 'rouler', 'super', 'servent', 'daction', 'lorsque', 'timebased', 'receiving', 'encyclopedia', 'january', 'shotaro', 'progresser', 'humain', 'disk', 'pologne', 'inclut', 'autre', 'mixture', 'septemberlimited', 'doreilles', 'rendered', 'magazines', 'times', 'summer', 'dosados', 'paysil', 'humaine', 'sans', 'believed', 'australia', 'afin', 'anciens', 'officially', 'good', 'zoras', 'indiquant', 'when', 'holder', 'founder', 'pendant', 'introduit', 'rosy', 'appearing', 'nordique', 'longues', 'depossedee', 'humanoid', 'rongeurs', 'montre', 'mondeocean', 'celuici', 'location', 'stars', 'enemy', 'minishs', 'industry', 'computeranimated', 'pouvoir', 'echanger', 'prochain', 'solving', 'senrichit', 'secondairesimage', 'remakesnintendo', 'ressuscite', 'details', 'prosperity', 'squareenix', 'appearance', 'naughty', 'pinball', 'erafennec', 'existed', 'multijoueurversions', 'lorion', 'seriess', 'imperium', 'holds', 'score', 'donnes', 'gamesas', 'hytopia', 'capacityboard', 'maybe', 'rewarded', 'crossing', 'accompagnes', 'chez', 'fleurs', 'relives', 'multiples', 'aired', 'port', 'nintendocreators', 'centre', 'environnant', 'symboles', 'considerablement', 'arielle', 'litteralement', 'exploring', 'fruition', 'celshaded', 'music', 'various', 'spoken', 'doom', 'lists', 'annual', 'avoided', 'george', 'nordamericaine', 'choisi', 'wand', 'poules', 'retrieved', 'interaction', 'copie', 'oeufs', 'equipment', 'illes', 'seriesa', 'opposed', 'metacritic', 'profit', 'systeme', 'possedent', 'petites', 'detaillee', 'mipoissons', 'retained', 'kollar', 'verts', 'stereoscopic', 'format', 'doree', 'waker', 'manchots', 'zeldamain', 'nondance', 'focusing', 'fils', 'lite', 'cinematiquesdautres', 'etatsunis', 'testeurs', 'jourla', 'removed', 'realise', 'images', 'influence', 'hostiles', 'learns', 'incluse', 'dingo', 'zeldathe', 'side', 'manual', 'prisonniers', 'bouclier', 'scenarios', 'mishouzaki', 'performed', 'form', 'enterprises', 'berghammer', 'situe', 'considered', 'brief', 'suite', 'masks', 'consolethe', 'lemploi', 'library', 'abattu', 'anime', 'simplement', 'toutes', 'considere', 'prize', 'tresors', 'famicoms', 'jeux', 'nelsonic', 'montagnes', 'roster', 'require', 'dengeki', 'platinum', 'games', 'essential', 'dexperience', 'reussie', 'dungeon', 'paradise', 'wolfpromotional', 'complicated', 'fully', 'droit', 'midona', 'dark', 'rallient', 'crossedover', 'tenue', 'aurait', 'certain', 'gamesindustry', 'genta', 'copy', 'vividlyrealised', 'crystal', 'productions', 'creations', 'representant', 'chestin', 'bonnet', 'generations', 'normale', 'incorporates', 'kondo', 'warriors', 'lautre', 'embrace', 'vestal', 'reorchestrees', 'days', 'audio', 'focuses', 'marchand', 'bourgeon', 'under', 'tallarico', 'zeldatotilo', 'kozuo', 'jason', 'select', 'alexander', 'identity', 'objet', 'lying', 'canonmain', 'entre', 'expulsees', 'doreesannees', 'baguette', 'lesprit', 'etoiles', 'entries', 'sequence', 'composer', 'nesthe', 'inedit', 'pointu', 'royaume', 'free', 'kondokoji', 'vegetale', 'horse', 'developpement', 'mcdonald', 'poulpes', 'temple', 'quils', 'birth', 'rescuing', 'collector', 'included', 'fights', 'motifs', 'poured', 'mouths', 'selling', 'reputes', 'hyrules', 'powers', 'selon', 'turnbased', 'itself', 'title', 'plastic', 'stephen', 'subrosiens', 'just', 'usually', 'seule', 'graphiquement', 'optionalfour', 'noted', 'third', 'praised', 'mobygames', 'decide', 'adult', 'contenant', 'japans', 'correspond', 'larc', 'historia', 'soulcalibur', 'japonle', 'attaque', 'paralyze', 'textbook', 'rest', 'place', 'nintendo', 'marvel', 'notes', 'secrets', 'lance', 'comporte', 'verification', 'perilmais', 'wife', 'influenced', 'here', 'confere', 'beaucoup', 'mike', 'marchands', 'possedant', 'platinumgames', 'comment', 'copies', 'logo', 'despite', 'nombre', 'crucial', 'enabled', 'michemin', 'lionhead', 'transform', 'horrifying', 'voice', 'canada', 'trackers', 'ready', 'exactement', 'senses', 'souhaitent', 'seven', 'serieemblemeles', 'move', 'eshop', 'triangle', 'travers', 'across', 'defeat', 'alternate', 'nonplayer', 'relic', 'sauver', 'subscribing', 'capture', 'identify', 'renewing', 'forme', 'lannee', 'booklet', 'centuries', 'vastes', 'doiseau', 'janvier', 'duel', 'mouvements', 'sends', 'imagination', 'instrument', 'explication', 'percevoir', 'inspire', 'todd', 'nord', 'grand', 'maskthe', 'dungeons', 'task', 'connues', 'influenceevery', 'need', 'tues', 'gouverner', 'chili', 'realm', 'impa', 'ancient', 'spike', 'built', 'faroriaennemisimage', 'ville', 'east', 'often', 'films', 'chosen', 'shown', 'reactions', 'allowing', 'item', 'lieu', 'button', 'feelings', 'deplacement', 'voire', 'unproduced', 'garden', 'shigeru', 'maison', 'entire', 'livres', 'disponibles', 'hyrulean', 'speciales', 'knows', 'europe', 'mabinogion', 'medievale', 'approfondissant', 'sablier', 'protect', 'peut', 'femme', 'bien', 'sages', 'dite', 'three', 'celestriers', 'dealing', 'nait', 'descendants', 'lockon', 'predecessor', 'recoit', 'connect', 'identique', 'contraignant', 'commercially', 'filmsin', 'tant', 'dotee', 'meter', 'mini', 'others', 'miniboss', 'persia', 'returns', 'ciel', 'grunts', 'monster', 'hante', 'seriesmain', 'entouree', 'sauve', 'virtues', 'downloads', 'located', 'stalfos', 'habitant', 'portrayed', 'eighth', 'remaster', 'canon', 'videos', 'venerable', 'avatar', 'monnaie', 'history', 'personnalise', 'becoming', 'developer', 'ganonganon', 'yoshiki', 'marquant', 'tyrant', 'confirmee', 'espece', 'switch', 'note', 'vieslieuximage', 'silvestre', 'cohabiter', 'tournant', 'studies', 'anniversary', 'transforme', 'purpose', 'spacey', 'vanpool', 'avant', 'level', 'final', 'hatred', 'assist', 'petits', 'ressemble', 'theorie', 'otherwiseimpassable', 'reeditions', 'francaise', 'acclaim', 'sell', 'quune', 'eternally', 'lentree', 'always', 'bloodsoaked', 'amicaux', 'exclusive', 'gaming', 'aneantir', 'campaign', 'seulement', 'legendes', 'troublesome', 'darker', 'widely', 'electronic', 'brilliance', 'mygames', 'souvent', 'cable', 'graphique', 'tres', 'perform', 'awarded', 'pourtant', 'reunited', 'sylvestre', 'originally', 'purchasing', 'doute', 'annexes', 'cieux', 'avancee', 'radio', 'reason', 'great', 'difficile', 'contraint', 'novateur', 'epoque', 'donner', 'publiee', 'based', 'cette', 'categorie', 'control', 'multitude', 'wanted', 'learned', 'orchestral', 'humains', 'fans', 'sword', 'playable', 'impact', 'propres', 'parts', 'explained', 'motionblur', 'small', 'manette', 'character', 'regions', 'corps', 'lechec', 'exemplairesla', 'torres', 'actionquand', 'last', 'cartoons', 'cultures', 'recherche', 'consists', 'involve', 'macdonald', 'produits', 'golden', 'wired', 'gamesclarification', 'aroo', 'archway', 'creatures', 'predecessors', 'split', 'integre', 'nombreuses', 'calibur', 'natural', 'exploits', 'follow', 'jouer', 'ultimately', 'profile', 'vegetaux', 'before', 'several', 'frequently', 'rolling', 'auto', 'raphael', 'critiques', 'boule', 'seriesfollowing', 'tracks', 'huit', 'kayali', 'wind', 'peters', 'news', 'blocked', 'griseocarina', 'disposition', 'perdus', 'gameboy', 'showed', 'unlockable', 'tinker', 'vers', 'accrues', 'linkproduits', 'main', 'luke', 'available', 'solely', 'paru', 'sousboss', 'kokiri', 'hylians', 'battle', 'plague', 'cast', 'reconnaitre', 'book', 'joueurthe', 'cartouche', 'converted', 'during', 'privee', 'kotaku', 'cologne', 'veut', 'franchise', 'arrangement', 'ancestors', 'journey', 'bombes', 'pourrait', 'bulbins', 'service', 'should', 'publication', 'mailed', 'juin', 'mixing', 'very', 'droits', 'ames', 'lexpansion', 'dessai', 'handed', 'screwattack', 'avoir', 'ombre', 'levels', 'milieu', 'biggoron', 'layouts', 'moyens', 'reveille', 'paysage', 'felt', 'lloyd', 'caledfwlch', 'targeting', 'subsequently', 'devient', 'contentant', 'apparence', 'trilogie', 'chris', 'shards', 'xplay', 'goddessnintendo', 'concentre', 'engloutie', 'fees', 'menacing', 'producers', 'gros', 'struggle', 'avance', 'director', 'upon', 'rocheux', 'neededa', 'princessin', 'fighter', 'souligner', 'marais', 'divine', 'egares', 'acheter', 'allowed', 'entry', 'anniversaire', 'board', 'range', 'deux', 'statements', 'sentient', 'wolf', 'hall', 'five', 'entertainment', 'feminin', 'factorydans', 'cyberpunk', 'seed', 'inhouse', 'communication', 'trip', 'threat', 'mode', 'characteristically', 'resides', 'originaires', 'voler', 'imagi', 'ressemblant', 'loriens', 'lextension', 'back', 'baton', 'upcom', 'creee', 'turnnintendo', 'disparition', 'goddesses', 'connection', 'geography', 'pete', 'deep', 'empecher', 'shrink', 'appear', 'search', 'forwards', 'announced', 'feter', 'standing', 'dhyrulehistorique', 'presumably', 'lacquisition', 'with', 'mirror', 'publies', 'sense', 'autour', 'rire', 'univers', 'bleules', 'epee', 'ueda', 'faire', 'tornade', 'tokyo', 'affixed', 'moving', 'plays', 'born', 'renforce', 'appelee', 'modifie', 'avoid', 'rides', 'caracteristiques', 'changing', 'since', 'flowers', 'original', 'long', 'fairy', 'digitally', 'kamigami', 'containing', 'luimeme', 'hiatus', 'adaptation', 'whalen', 'hommage', 'ashes', 'references', 'lave', 'trigger', 'remaniement', 'entrainant', 'land', 'recurrent', 'stage', 'reliable', 'forward', 'revamped', 'terrains', 'fantome', 'niveau', 'system', 'user', 'fell', 'unusnzleusazeldas', 'unchanged', 'primaire', 'train', 'transformed', 'focused', 'dementi', 'creature', 'save', 'chronologythe', 'agressivite', 'symphoniquepour', 'zonedans', 'bearers', 'game', 'wants', 'populaire', 'fiveyear', 'technique', 'assemblages', 'harris', 'traversees', 'rereleases', 'they', 'pahya', 'reportmcmillan', 'dapparence', 'importants', 'gannett', 'sagesse', 'reprise', 'parfois', 'lexploration', 'watch', 'competitionas', 'serieen', 'again', 'selfcontained', 'canceledbefore', 'sorti', 'pres', 'incentive', 'label', 'derives', 'indispensables', 'actionaventure', 'legende', 'pouvait', 'creant', 'croyant', 'cote', 'immense', 'coquillages', 'moins', 'presque', 'tower', 'alchimie', 'tribu', 'links', 'grises', 'edite', 'omnipotent', 'cest', 'resume', 'rebuild', 'slightly', 'satoru', 'tablets', 'aller', 'ancestrales', 'entirety', 'brad', 'europethe', 'disappointed', 'continue', 'facilement', 'precise', 'premieres', 'forteresse', 'realiste', 'shockers', 'uhors', 'wildlors', 'force', 'deity', 'insert', 'presse', 'proof', 'remainder', 'utiles', 'influences', 'existe', 'comble', 'davies', 'peuple', 'where', 'advice', 'inconnue', 'difficulty', 'sagit', 'londres', 'spectre', 'dutton', 'otero', 'after', 'introduction', 'zeldaprincess', 'sought', 'korogus', 'melodic', 'remained', 'systemfirst', 'only', 'shading', 'publie', 'boss', 'breaks', 'realisme', 'oeuvres', 'many', 'piece', 'samus', 'seventhgreatest', 'partir', 'mido', 'handled', 'fechner', 'docarina', 'seeks', 'sales', 'linteret', 'precarious', 'ennemies', 'doit', 'detailed', 'plotline', 'ended', 'scores', 'savoir', 'diffusees', 'december', 'theres', 'partie', 'septembre', 'combattre', 'zeldapour', 'crushed', 'minish', 'nuages', 'quocarina', 'though', 'somearea','thearea','arena', 'capcom', 'relativement', 'once', 'vivre', 'heures', 'releases', 'twilight', 'portal', 'british', 'mirrored', 'light', 'there', 'ubisoft', 'doresla', 'drops', 'joueur', 'perche', 'disposant', 'external', 'tires', 'reussi', 'roles', 'designers', 'zeldalink', 'discarding', 'changed', 'mask', 'donjongeneralement', 'problematique', 'footage', 'comme', 'publisher', 'bois', 'existsince', 'quest', 'exterieurcaverne', 'photo', 'reaver', 'ronaghan', 'celle', 'actuels', 'autant', 'distributed', 'charactersin', 'etait', 'represente', 'interagissent', 'ailleurs', 'semble', 'demployer', 'courage', 'tunique', 'facile', 'swordplay', 'pause', 'guardian', 'dedicated', 'wayne', 'rate', 'monthly', 'comprenant', 'planned', 'troubles', 'zone', 'doors', 'rendre', 'phantom', 'double', 'produite', 'connait', 'titres', 'doreetous', 'intervenir', 'action', 'lombre', 'previously', 'teleportation', 'borrowed', 'allumniation', 'preorder', 'commercialise', 'poorly', 'sometime', 'birthday', 'flute', 'thomas', 'parti', 'evil', 'devait', 'replaced', 'hennig', 'specialises', 'auparavant', 'pushed', 'traditional', 'boken', 'earliest', 'made', 'quelle', 'maskle', 'give', 'isbn', 'locales', 'playing', 'respectivelyin', 'ezlo']
tmplst = []

gcnt = 718233
save = "utnc"
for item in lst:
     if not item.upper() in tmplst:
          tmplst.append(item.upper())
lst = tmplst
uniq = []
loaded = 0

def brute(string, length, charset,encrypted):
    global gcnt
    global loaded
    cryptcnt = 1

    if len(string) == length:
        return
    for char in charset:
        temp = string + char
#        print(temp)        
        #if 1 == 1:
        if temp == save or loaded == 1:
            loaded = 1
#            print(temp)
            for crypt in encrypted:

                if cryptcnt >6:
                    cryptcnt = 1

                if cryptcnt == 1:
                    precision = " No Modif ."
                if cryptcnt == 2:
                    precision = " No Codon ."
                if cryptcnt == 3:
                    precision = " No Codon +U ."
                if cryptcnt == 4:
                    precision = " With Codon ."
                if cryptcnt == 5:
                    precision = " With Codon + M "
                if cryptcnt == 6:
                    precision = " With Codon + M + U "
                cle = temp

                gkey = []
                for num in str(gcnt):
                    gkey.append(int(num))
                gcnt = gcnt +1

                col = pycipher.ColTrans(cle).decipher(crypt)

                gron = pycipher.Gronsfeld(gkey).decipher(crypt)

                vigen = pycipher.Vigenere(cle).decipher(crypt) 

                bof = pycipher.Beaufort(cle).decipher(crypt)

                auto = pycipher.Autokey(cle).decipher(crypt)

                port = pycipher.Porta(cle).decipher(crypt)

                bingo = 0
                bingopass = 0
               
                for mot in lst:

                  if len(mot) >= 3 and len(mot) <= 5 and mot in col:
                       bingo = bingo + 1
                  if len(mot) >= 3 and len(mot) <= 5 and mot in vigen:
                       bingo = bingo + 1
                  if len(mot) >= 3 and len(mot) <= 5 and mot in gron:
                       bingo = bingo + 1
                  if len(mot) >= 3 and len(mot) <= 5 and mot in auto:
                       bingo = bingo + 1
                  if len(mot) >= 3 and len(mot) <= 5 and mot in port:
                       bingo = bingo + 1
                  if len(mot) >= 3 and len(mot) <= 5 and mot in bof:
                       bingo = bingo + 1

                  if bingo > 6:
                        bingopass = 1
                  else:
                        bingopass = 0

                  #print(bingo)
                #for mot in lst:
                  if mot in col and len(mot) > 5 and mot not in uniq:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Coltranfert===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(cle))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(col))
                              myfile.write("\n")

                       print("===Coltranfert===")
                       print("==="+precision+"===")
                       if cle in lst:
                           print("Clé présente également dans le dico : ",cle)
                       else:
                           print("Clé : ",cle)
                           
                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()

                       #print("Clé : ",cle)
                       #print()
                       print(col)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                       #uniq.append(mot)

                  if mot in col and bingopass == 1:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Coltranfert===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(cle))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(col))
                              myfile.write("\n")

                       print("===Coltranfert===")
                       print("==="+precision+"===")
                       if cle in lst:
                           print("Clé présente également dans le dico : ",cle)
                       else:
                           print("Clé : ",cle)

                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()

                       #print("Clé : ",cle)
                       #print()
                       print(col)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                       #uniq.append(mot)

                  if mot in gron and len(mot) > 5 and mot not in uniq:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Gronsfeld===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(gkey))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(gron))
                              myfile.write("\n")

                       print("===Gronsfeld===")
                       print("==="+precision+"===")
                       if gkey in lst:
                           print("Clé présente également dans le dico : ",gkey)
                       else:
                           print("Clé : ",gkey)

                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()

                       #print("Clé : ",gkey)
                       #print()
                       print(gron)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                       #uniq.append(mot)

                  if mot in gron and bingopass == 1:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Gronsfeld===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(gkey))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(gron))
                              myfile.write("\n")

                       print("===Gronsfeld===")
                       print("==="+precision+"===")
                       if gkey in lst:
                           print("Clé présente également dans le dico : ",gkey)
                       else:
                           print("Clé : ",gkey)

                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()

                       #print("Clé : ",gkey)
                       #print()
                       print(gron)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                       #uniq.append(mot)


                  if mot in vigen and len(mot) > 5 and mot not in uniq:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Vigenere===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(cle))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(vigen))
                              myfile.write("\n")

                       print("===Vigenere===")
                       print("==="+precision+"===")
                       if cle in lst:
                           print("Clé présente également dans le dico : ",cle)
                       else:
                           print("Clé : ",cle)

                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()

                       #print("Clé : ",cle)
                       #print()
                       print(vigen)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                       #uniq.append(mot)


                  if mot in vigen and bingopass == 1:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Vigenere===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(cle))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(vigen))
                              myfile.write("\n")

                       print("===Vigenere===")
                       print("==="+precision+"===")
                       if cle in lst:
                           print("Clé présente également dans le dico : ",cle)
                       else:
                           print("Clé : ",cle)

                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()

                       #print("Clé : ",cle)
                       #print()
                       print(vigen)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                       #uniq.append(mot)


                  if mot in bof and len(mot) > 5 and mot not in uniq:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Beaufort===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(cle))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(bof))
                              myfile.write("\n")

                       print("===Beaufort===")
                       print("==="+precision+"===")
                       if cle in lst:
                           print("Clé présente également dans le dico : ",cle)
                       else:
                           print("Clé : ",cle)
                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()


                       #print("Clé : ",cle)
                       #print()
                       print(bof)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                       #uniq.append(mot)

                  if mot in bof and bingopass == 1:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Beaufort===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(cle))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(bof))
                              myfile.write("\n")

                       print("===Beaufort===")
                       print("==="+precision+"===")
                       if cle in lst:
                           print("Clé présente également dans le dico : ",cle)
                       else:
                           print("Clé : ",cle)
                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()


                       #print("Clé : ",cle)
                       #print()
                       print(bof)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                       #uniq.append(mot)


                  if mot in auto and len(mot) > 5 and mot not in uniq:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Autokey===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(cle))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(auto))
                              myfile.write("\n")

                       print("===Autokey===")
                       print("==="+precision+"===")
                       if cle in lst:
                           print("Clé présente également dans le dico : ",cle)
                       else:
                           print("Clé : ",cle)
                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()

                       #print("Clé : ",cle)
                       #print()
                       print(auto)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                       #uniq.append(mot)


                  if mot in auto and bingopass == 1:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Autokey===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(cle))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(auto))
                              myfile.write("\n")

                       print("===Autokey===")
                       print("==="+precision+"===")
                       if cle in lst:
                           print("Clé présente également dans le dico : ",cle)
                       else:
                           print("Clé : ",cle)
                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()

                       #print("Clé : ",cle)
                       #print()
                       print(auto)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                       #uniq.append(mot)





                  if mot in port and len(mot) > 5 and mot not in uniq:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Porta===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(cle))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(port))
                              myfile.write("\n")

                       print("===Porta===")
                       print("==="+precision+"===")
                       if cle in lst:
                           print("Clé présente également dans le dico : ",cle)
                       else:
                           print("Clé : ",cle)
                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()



                       #print("Clé : ",cle)
                       #print()
                       print(port)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                #cryptcnt = cryptcnt +1
                       #uniq.append(mot)

                  if mot in port and bingopass == 1:

                       #print("==")

        #               print("FOUND SOMETHING !!")
                       with open('Vrute.result', 'a') as myfile:
                              myfile.write("===Porta===")
                              myfile.write("==="+precision+"===")
                              myfile.write("Clé :"+str(cle))
                              myfile.write("Bingo: "+str(bingo))
                              myfile.write(str(port))
                              myfile.write("\n")

                       print("===Porta===")
                       print("==="+precision+"===")
                       if cle in lst:
                           print("Clé présente également dans le dico : ",cle)
                       else:
                           print("Clé : ",cle)
                       print("Mot : ",mot)
                       if bingo > 0:
                            print("Bingo : ",bingo)
                            print()



                       #print("Clé : ",cle)
                       #print()
                       print(port)


                       print("==")
                       bingo = bingo +1
                       #time.sleep(3)

                cryptcnt = cryptcnt +1
                       #uniq.append(mot)

       
    ##
        brute(temp, length, charset,cipherlist)
    ##

#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alpha = "abcdefghijklmnopqrtuvwxyz"
#cipher = "nl mhv ke iczsx gzt fcvw"
cipherlist = ["MQESWYVPBADMNLYRFJGHPGTWWFIPRIBROIOIEMNQPGXBJAJRFTKVRWPBABWPEXDXKARIPGASWSSCHLIVVGQMDWRDNCLCAOPHTMWPOWXXTWEOCHLMIEIFXPJGNPDTCARGJQCLCFLDIRHFKGQSIGFDILFSYSOQLOWCHPICSYEGGOODBKHGBVXVJOQHDMRHBQRTSRJWHN","QESWYVPBADMNLYRFJGHPGTWWFIPRIBROIOIEMNQPGXBJAJRFTKVRWPBABWPEXDXKARIPGASWSSCHLIVVGQMDWRDNCLCAOPHTMWPOWXXTWEOCHLMIEIFXPJGNPDTCARGJQCLCFLDIRHFKGQSIGFDILFSYSOQLOWCHPICSYEGGOODBKHGBVXVJOQHDMRHBQRTSRJWHN","QESWYVPBADMNLYURFJGHPGTWWFIPRIBUROIOIEMNQPGXBJAJRFTKVRWPBABWPEXDXKARIPGASWSSCUHLIVVGQMDWRDNCLUCAOPHTMWPOWXXTWEOCHLUMIEIFXPJGNPDTCARGJQCLCFLDIRUHFKGQSUIGFDILFSYSOQLOWCHPICUSYEGGOODBKHGBVXVJOQHDMRHBQRTSRJWUHNU","AUGQESWYVPBADMNLYUGARFJGHPGTWWFIPRIBUGAROIOIEMNQPGXBJAJRFTKVRWPBABWPEXDXKARIPGASWSSCUGAHLIVVGQMDWRDNCLUGACAOPHTMWPOWXXTWEOCHLUGAMIEIFXPJGNPDTCARGJQCLCFLDIRUGAHFKGQSUGAIGFDILFSYSOQLOWCHPICUGASYEGGOODBKHGBVXVJOQHDMRHBQRTSRJWUGAHNUAG","MQESWYVPBADMNLYUGARFJGHPGTWWFIPRIBUGAROIOIEMNQPGXBJAJRFTKVRWPBABWPEXDXKARIPGASWSSCUGAHLIVVGQMDWRDNCLUGACAOPHTMWPOWXXTWEOCHLUGAMIEIFXPJGNPDTCARGJQCLCFLDIRUGAHFKGQSUGAIGFDILFSYSOQLOWCHPICUGASYEGGOODBKHGBVXVJOQHDMRHBQRTSRJWUGAHNUAG","MQESWYVPBADMNLYURFJGHPGTWWFIPRIBUROIOIEMNQPGXBJAJRFTKVRWPBABWPEXDXKARIPGASWSSCUHLIVVGQMDWRDNCLUCAOPHTMWPOWXXTWEOCHLMIEIFXPJGNPDTCARGJQCLCFLDIRUHFKGQSUIGFDILFSYSOQLOWCHPICUSYEGGOODBKHGBVXVJOQHDMRHBQRTSRJWUHNU"]

max = 5

#print("Starting Bruteforce of : ")
#print(cipher)
#print("Max key lenght : ",max)

print()

cnt = 1
while cnt <= max:
     print("Starting Bruteforce of : ")
     print()
     print(cipherlist)
     print()
     print()
     print("Max key lenght : ",max)
     print()
     print("Current key lenght :",cnt)
     print()
     brute("", cnt, alpha,cipherlist)
     cnt = cnt +1



