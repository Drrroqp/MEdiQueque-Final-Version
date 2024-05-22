gsap.registerPlugin(ScrollTrigger, ScrollSmoother)

if (ScrollTrigger.isTouch !==1){

    ScrollSmoother.create({
        wrapper: "wrapper",
        content: "content",
        smooth: 1.3,
        effects: true
    })

    let itemsL = gsap.utils.toArray(".columblockinfo1 .block-1")

    itemsL.forEach(item => {
        gsap.fromTo(item, {x: -200, opacity: 0}, {
            opacity: 1, x: 0,
            scrollTrigger:{
                trigger: item,
                start: -700,
                end: 0,
                scrub: true
            }
        })
    })

    let itemsR = gsap.utils.toArray(".columblockinfo2 .block-1")

    itemsR.forEach(item => {
        gsap.fromTo(item, {x: 200, opacity: 0}, {
            opacity: 1, x: 0,
            scrollTrigger:{
                trigger: item,
                start: -700,
                end: 0,
                scrub: true
            }
        })
    })

}