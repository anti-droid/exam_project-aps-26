A fractal 

Vigtig observation:
- Hver segments længde vil stige med en faktor 'a' for hver fraktal grad
- Vi kan dermed udlede på hvilken segment vi er på ved at 
- derefter kan vi finde hvilet linjestykke vi er på i faktalen



Dataload:
- finder forholdne imellem de forskellige linje segmenter og summen af hele polylinjen (måske også i forhold til korteste afstand imellem start og slut punkt)

- finder vinklerne imellem punkterne og gemmer disse (they are a suprise tool we are gonna use for later)



Løsning:
1. traverser polilinjen af første grad indtil vi ender på et linjesegment vi ikke kan treversere fuldt ud (fordi vi ikke kan nå langt nok)
2. nu er vores start og slut punkt, start og slut punktet på det linjesegment vi ikke kunne treversere fuldt
3. vi beregner afstanden imellem de to punkter
- recursively repeat sep 1.-3.
5. når vi er nået sidste grad vi skal regne ifølge opgaven skal vi finde det præcises punkt vi ender på