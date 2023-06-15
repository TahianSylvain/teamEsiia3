
/*  EXEMPLE
 
    new Carousel = document.querySelector("#carousel1")
    otr'zao ny structure-n'ny instance iray:

    <div id="carousel1">                       -> element
        <div class="root_carousel">            -> root
            <div class="carousel_container">   -> container
                <div class="carousel_item">    -> item
                    <div class="item"></div>   -> child 1
                </div>
                -----------------------------------------
                -----------------------------------------
            </div>
        </div>
    </div>
*/


class Carousel {

    /**
     * 
     * @param {HTMLElement} element 
     * @param {Object} options
     * @param {Number} [options.slidesToScroll=1] isan'ny card ahisaka
     * @param {Number} [options.slidesToShow=1] isan'ny card miseho
     * @param {Boolean} [options.infinite=false] 
     * @param {Boolean} [options.automatic=false]
     */
    constructor (element, options = {}) {
        this.element = element
        this.options = Object.assign({}, {
            // propriété par defaut, raha vide lay options
            slidesToScroll: 1, 
            slidesToShow: 1,
            infinite: false,
            automatic: false
        }, options /* raha tsy vide */)

        this.isMobile = false

        // copier-na anaty tab "children" ireo zanak' "element" rehetra,
        // ankoatr'lay "root" creer-na etsy ambany
        let children = [].slice.call(element.children)

        // correction "slidesToShow" sy "slidesToScroll"
        // règle: "slidesToShow" <= "items.length" et "slidesToScroll" <= "slidesToShow"
        this.options.slidesToShow = (this.options.slidesToShow >= children.length)? children.length:this.options.slidesToShow
        this.options.slidesToScroll = (this.options.slidesToScroll > this.options.slidesToShow)? this.options.slidesToShow:this.options.slidesToScroll
        this.options.infinite = (this.options.automatic)?true:this.options.infinite

        // indice du premier item visible (item à gauche), 0 au debut
        this.curentItem = 0
        // créer <div class="root_container"></div>
        // 
        this.root = this._createDivWithClass('root_carousel')
        // créer <div class="carousel_container"></div>
        this.container = this._createDivWithClass('carousel_container')
        // element > root > container
        // container atao anaty root, dia root anaty element
        this.root.appendChild(this.container)
        this.element.appendChild(this.root)


        // créer tab "items" ametrahana ireo "div.carousel_item" (na "item") 
        // ampidirina anaty "item" ireo zanak' "element" (children)
        // avy eo atao anay "container" ireo "div.carousel_item"
        this.items = children.map((child) => {
            let item = this._createDivWithClass('carousel_item')
            item.appendChild(child)
            // this.container.appendChild(item)
            return item
        });

        if (this.options.infinite) {
            this.offset = this.slidesToShow + 1
            this.items = 
                this.items.slice(this.items.length - this.offset).map(item => item.cloneNode(true))
                .concat(this.items)
                .concat(this.items.slice(0, this.offset).map(item => item.cloneNode(true)));
            
            this.curentItem = this.offset 
            // console.log(this.curentItem)
            // console.log(this.items)
            
        }
        this.items.forEach(item => this.container.appendChild(item))

        this._setStyle()

        if (!this.options.automatic) {
            this._createNavigation()
        } else {
            this.container.style.transition = 'transform 1s'
            this.root.style.overflow = 'hidden'
            let auto = setInterval(() => {
                this._next()
            }, 8000)
            this.items.forEach(item => item.addEventListener(
                'mouseenter',
                ()=>{
                    clearInterval(auto)
                }
            ))
            this.items.forEach(item => item.addEventListener(
                'mouseleave',
                ()=>{
                    auto = setInterval(() => {
                        this._next()
                    },8000)
                }
            ))
        }
        this._gotoItem(this.curentItem, false)

        // if (this.options.infinite) {
        //     this.root.addEventListener('transitionend', this.resetInfinite.bind(this))
        // }

        this._onWindowResize()
        window.addEventListener('resize', this._onWindowResize.bind(this))

    }
    
    // methode anomezana width ny "container" sy "item"
    _setStyle () {
        // règle de trois fotsiny no miasa eto
        this.container.style.width = (
            this.items.length / this.slidesToShow * 100
        ) + "%"
        this.items.forEach(item => item.style.width = (100/this.items.length) + "%")
    }

    // methode pour créer les boutons next et prev
    _createNavigation () {
        // rehefa "slidesToShow" < "items.length" vao misy button
        if (this.slidesToShow !== this.items.length) {
            this.nextButton = this._createDivWithClass('carousel_next')
            this.prevButton = this._createDivWithClass('carousel_prev')
            if (!this.options.infinite){
                this.prevButton.classList.add('hide')
            }
            this.root.appendChild(this.nextButton)
            this.root.appendChild(this.prevButton)
            this.nextButton.addEventListener('click', this._next.bind(this))
            this.prevButton.addEventListener('click', this._prev.bind(this))

            // methode "onMove" pour class "Carousel"
            // manafina ireo Button
            // antsoina any anaty "gotoItem" ty methode ty
            this._onMove = (index) => {
                if (index === 0){
                    this.prevButton.classList.add('hide')
                } else {
                    this.prevButton.classList.remove('hide')
                }
                if (index == this.items.length - this.slidesToShow) {
                    this.nextButton.classList.add('hide')
                } else {
                    this.nextButton.classList.remove('hide')
                }
            }
            
        }
    }
    _next () {    
        // --- manala espace vide any @ farany raha tsy mahafeno slidesToShow ny nbr item ---
        let nextIndex = this.curentItem + this.slidesToScroll
        let rightVisibleItem = this.slidesToShow - 1
        let rightItem_nextShow = this.curentItem + rightVisibleItem + this.slidesToScroll
           
        if (!this.options.infinite) {
            if (this.items[rightItem_nextShow] !== undefined) {
            nextIndex = this.curentItem + this.slidesToScroll
            } else {
            let i=1
            while (i<this.slidesToShow) {
                if (this.items[rightItem_nextShow -i] !== undefined) {
                    nextIndex = this.curentItem + (this.slidesToScroll -i)
                    break
                } else {
                    i++
                }
            }
        }
        }
        
         
        // ----------------------------------
        this._gotoItem(nextIndex)
        if (this.options.infinite /* this.curentItem < this.offset */) {
            this.root.addEventListener('transitionend', this._resetInfinite.bind(this))
        }

    }
    _prev () {
        // --- manala espace vide any @ voalohany...............
        let prevIndex = this.curentItem - this.slidesToScroll
        let leftItem_prevShow = this.curentItem - this.slidesToScroll
        
        if (!this.options.infinite) {
            if (this.items[leftItem_prevShow] !== undefined) {
            prevIndex = this.curentItem - this.slidesToScroll
            } else {
            prevIndex = 0
        }
        }
        
        // --------------------------

        this._gotoItem(prevIndex)
        if (this.options.infinite /* this.curentItem < this.offset */) {
            this.root.addEventListener('transitionend', this._resetInfinite.bind(this))
        }

    }

    /** 
     * déplace le carousel vers l'élement cible
     * @param {Number} index
     * @param {Boolean} [animate=true] 
     */
    _gotoItem (index, animate = true) {
        /* if (index < 0) {
            index = this.items.length - this.options.slidesToShow
        } else if (index >= this.items.length || this.items[this.curentItem + this.options.slidesToShow ] === undefined) {
            console.log(index >= this.items.length)
            console.log(this.curentItem)
            index = 0
        }  */
              

        // mihisaka index * item.width par rapport à l'axe X
        // valeur negatif (-100) car deplacement positif: droite vers gauche
        let translateX = index * -100 / this.items.length
        if (animate === false) {
            this.container.classList.add('stop_transition')
        }
        this.container.style.transform = 'translateX(' + translateX + '%)'
        this.container.offsetHeight
        
        this.curentItem = index
        // console.log("=>"+this.curentItem)
        if (!this.options.infinite) {
            this._onMove(index)
        }
        if (animate === false) {
            this.container.classList.remove('stop_transition')
        }
        
    }

    // infinite illusion
    _resetInfinite () {
        if (this.curentItem < this.slidesToScroll) {
            // console.log("1:"+this.curentItem)
            this._gotoItem((this.curentItem + (this.items.length - 2 * this.offset)), false)
        } 
        else if (this.curentItem > this.items.length - 2 * this.offset) {
            // console.log("2:"+this.curentItem)
            this._gotoItem((this.curentItem - (this.items.length - 2 * this.offset)), false)
        }
    }

    /**
     * 
     * @param {String} className
     * @returns {HTMLElement} 
     */
    _createDivWithClass (className) {
        let div = document.createElement('div')
        div.setAttribute('class', className)
        return div
    }

    _onWindowResize() {
        let mobile = window.innerWidth < 800
        // console.log(window.innerWidth);
        if(mobile !== this.isMobile) {
            // console.log("mobile");
            this.isMobile = mobile
            this._setStyle()
        }
    }

    get slidesToScroll() {
        return this.isMobile? 1: this.options.slidesToScroll
    }
    get slidesToShow() {
        return this.isMobile? 1: this.options.slidesToShow
    }
    /**
     * @param {(arg0: number) => void} number
     */
    _setSlidesToShow(number) {
        return this.options.slidesToShow = number
    }

}




document.addEventListener('DOMContentLoaded', function() {

    // instances Carousel
    new Carousel(document.querySelector('.slide'), {
        slidesToScroll: 1,
        slidesToShow: 1,
        automatic: true
        // infinite: true
    })
    
    // new Carousel(document.querySelector('.new_course_slide'), {
    //     slidesToScroll: 1,
    //     slidesToShow: 3,
    //     automatic: true
    //     // infinite: true
    // })
        
})

// new Carousel(document.querySelector('.courses_container'), {
//     slidesToScroll: 2,
//     slidesToShow: 4
// })
// let BTC = new Carousel(document.querySelector('.teacher_container'), {
//     slidesToScroll: 1,
//     slidesToShow: 5,
// })

// BTC._setSlidesToShow(5)
// BTC._setStyle()
// if(window.innerWidth < 1120) {
//     BTC._setSlidesToShow(4)
//     BTC._setStyle()
// }
// else {
//     BTC._setSlidesToShow(5)
//     BTC._setStyle()
// }
//  if(window.innerWidth < 950) {
//     BTC._setSlidesToShow(3)
//     BTC._setStyle()
// }
// window.addEventListener('resize', () => {
//     if(window.innerWidth < 1120) {
//         BTC._setSlidesToShow(4)
//         BTC._setStyle()
//     }
//     else {
//         BTC._setSlidesToShow(5)
//         BTC._setStyle()
//     }
//      if(window.innerWidth < 950) {
//         BTC._setSlidesToShow(3)
//         BTC._setStyle()
//         console.log(true);
//     }
// })
    

