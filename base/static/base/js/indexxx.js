function _$(elets) { return document.querySelector(elets) }
function _$$(setElets) { return document.querySelectorAll(setElets) }

// INITIALISATION RESPONSIVE
let isMobile = (window.innerWidth<=800)?true:false
function _mobileStyle() {
    _$('.topbar').style.padding = '0px 30px'
    _$('nav').style.top = (window.outerHeight - _$('nav').clientHeight) /2 + 'px'
    _$('.topbar_btn a:nth-child(1) i').setAttribute('class', 'ri-login-box-line')
    _$('.menu_btn_container').style.display = 'flex' 
}
if (isMobile) {
    _mobileStyle()
}

// RESPONSIVE
window.addEventListener('resize', () => {
    if (window.innerWidth <= 800) {
        isMobile = true
        _mobileStyle()
    } else {
        _$('.topbar').style.padding = '0px 70px'
        _$('.topbar_btn a:nth-child(1) i').setAttribute('class', 'ri-user-line')
        _$('nav').classList.remove('show')
        _$('.menu_btn_container').style.display = 'none'
    }
})

// SIDEBAR NAVIGATION ON MOBILE
let clicked = false
_$('.menu_btn_container').addEventListener('click', () => {
    if(!clicked) {
        _$('nav').classList.add('show')
    } else {
        _$('nav').classList.remove('show')
    }
    clicked = !clicked
})
document.addEventListener('click', (e) => {
    if (e.target.className !== 'menu_btn_container' && e.target.className !== 'menu_btn') {
        _$('nav').classList.remove('show')
    }
})

// STYLE TOPBAR ON SCROLL
let scrollValue = window.scrollY
if (scrollValue !== 0) {
    _$('.topbar').classList.add('scroll')
}
function _onLoad () {
    if (scrollValue !== 0) {
        _$('.topbar').style.transition = '0s'
        _$('.topbar').style.top = '0px'
    }
}
window.addEventListener('load', _onLoad)

function _onScroll() {
    window.removeEventListener('load', _onLoad)
    // _$('.topbar').style.transition = 'all 0.5s, top 0.5s 1.9s'
    scrollValue = window.scrollY
    if (scrollValue === 0) {
        _$('.topbar').classList.remove('scroll')
        // let links = _$('.link').children
        // for( let link of links) {   
        // }
        // _$('a[href="#home"]').classList.add('active')
    } else {
        _$('.topbar').classList.add('scroll')
    }
    if (scrollValue > _$('.content_desc').clientHeight - _$('.topbar').clientHeight*2) {
        _$('.logo_img img').setAttribute('src', "static/base/img/lvlind9.webp")
        _$('.topbar').classList.add('change_color')
    } else {
        _$('.logo_img img').setAttribute('src', "static/base/img/lvlind10.webp")
        _$('.topbar').classList.remove('change_color')
    }
}

window.addEventListener('scroll', _onScroll)


// let lvlind_svg = _$('#lvlind_svg path')
// console.log(lvlind_svg.getTotalLength());

// WAVE ANIMATION ON SCROLL

class Wave {
    /**
     * 
     * @param {HTMLElement} element 
     */
    constructor(element) {
        this.wave_container = element  
        let waves = element.children

        this.$1 = waves[0]
        this.$2 = waves[1]
        this.$3 = waves[2]

        if(isMobile){
            this.$1.style.setProperty('--w1', 100 + 'px')
            this.$2.style.setProperty('--w2', 200 + 'px')
            this.$3.style.setProperty('--w3', 300 + 'px')
        } else {
            this.$1.style.setProperty('--w1', -260 + 'px')
            this.$2.style.setProperty('--w2', -510 + 'px')
            this.$3.style.setProperty('--w3', -20 + 'px')
        }
        window.addEventListener('scroll', () => {
            let value = window.scrollY
            // console.log(value);
            // _$$('.wave').forEach((wave) => {
            //     wave.style.animation = 'none'
            // })
            if(isMobile){
                this.$1.style.setProperty('--w1', 100 + value * 5 + 'px')
                this.$2.style.setProperty('--w2', 200 + value * -4 + 'px')
                this.$3.style.setProperty('--w3', 300 + value * 3 + 'px')
            } else {
                this.$1.style.setProperty('--w1', -260 + value * 5 + 'px')
                this.$2.style.setProperty('--w2', -510 + value * -4 + 'px')
                this.$3.style.setProperty('--w3', -20 + value * 3 + 'px')
            }
        })

    }
}
new Wave(_$('.header_wave'))

// new Wave(_$('.stat_wave_top'))
// new Wave(_$('.stat_wave'))
new Wave(_$('.footer_wave'))

// const onScrollStop = callBack => {
//     let isScrolling;
//     window.addEventListener('scroll', e => {
//         clearTimeout(isScrolling)
//         isScrolling = setTimeout(() => {
//             callBack()
//         }, 150)
//     })
// }

// onScrollStop(() => {
//     // console.log("aaaaa")
//     _$$('.wave').forEach((wave) => {
//         wave.style.animation = ''
//     })
// })

// TOPBAR LINK HOVER AND CLICK EFFECT
_$$('.link a').forEach((link) => {
    link.addEventListener('mouseover', () => {
        link.classList.add('hover')
    })
    link.addEventListener('mouseout', () => {
        link.classList.remove('hover')
    })
    link.addEventListener('click', function() {
        for(let sibling of this.parentNode.children) {
            if (sibling !== this) sibling.classList.remove('active')
        }
        this.classList.add('active')
    })
})



// ANIMATION ON SCROLL
// window.addEventListener('scroll', () => {
//     let aboutPosition = _$('.about').getBoundingClientRect().bottom
//     let statPosition = _$('.statistic_container').getBoundingClientRect().bottom
//     let devPosition = _$('.teams_section').getBoundingClientRect().bottom
//     let screenPosition = window.innerHeight + 300
//     if(aboutPosition < screenPosition) {
//         _$('.about').classList.add('about_show')
//     } else {
//         _$('.about').classList.remove('about_show')
//     }
//     if(!isMobile){
//         if(statPosition < screenPosition) {
//             _$$('.card').forEach(card => {
//                 card.style.transform = "scale(1)"
//             })
//             setTimeout(() => {
//                 _$(".prof_percent .circle").style.strokeDashoffset = 502 - (502 * (22 / 100))+ "px"
//                 _$$(".circle")[1].style.strokeDashoffset = 502 - (502 * (78 / 100))+ "px"
//             }, 500);
//         }else{
//             _$$('.card').forEach(card => {
//                 card.style.transform = ""
//             })
//             setTimeout(() => {
//                 _$$(".circle")[0].style.strokeDashoffset = 502+ "px"
//                 _$$(".circle")[1].style.strokeDashoffset = 502+ "px"
//             }, 500);
//         }
//     } else {
//         _$(".prof_percent .circle").style.strokeDashoffset = 502 - (502 * (22 / 100))+ "px"
//         _$$(".circle")[1].style.strokeDashoffset = 502 - (502 * (78 / 100))+ "px"
//     }
//     if(devPosition < screenPosition) {
//         _$$('.teams_section > div').forEach(div => {
//             div.classList.add('devShow')
//         })
//     } else {
//         _$$('.teams_section > div').forEach(div => {
//             div.classList.remove('devShow')
//         })
//     }

    
// })

// // CIRCULAR PROGRESS BAR
// // window.addEventListener('load', () => {
// //     _$$('.progress').forEach(item => {
// //         let percentElement = item.querySelector('.nbr')
// //         let percentage = parseFloat(percentElement.innerText)
// //         let count = 0
// //         let time = 2000 / percentage
// //         setInterval(() => {
// //             if(count == percentage){
// //                 clearInterval() 
// //             } else {
// //                 count += 1
// //                 percentElement.innerText = count
// //             }
// //             let circle = item.querySelector('.circle')
// //             circle.style.strokeDashoffset = 502 - (502 * (percentage / 100)) 
// //         }, time)
// //     })
// // })


// // window.addEventListener('scroll', progress)


// window.addEventListener('load', () => {
//     _$('header').style.top = 0
//     _$('.topbar').style.position = 'fixed'
//     _$('.topbar').style.top = 0
//     _$('.content_desc h1').style.top = 0
//     _$('.content_desc p').style.top = 0
//     _$('.content_desc a').style.top = 0
// })