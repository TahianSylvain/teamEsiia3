
/* ==== INITIALISATION ==== */
/* --- initialisation show/hide --- */
// let logWidth = (!isMobile)?500:window.innerWidth
// _$('.login').style.setProperty('--width', `${logWidth}px`)
// _$('.register').style.setProperty('--width', `${logWidth}px`)

// let login = false
// let register = false

// let gap = ((window.innerWidth - logWidth) / 2)
// _$('.log_reg_wrap').style.gap = `${gap}px`

/* --- initialisation registration step --- */
const formSteps = _$$('.form_step')
function _resetFormStepNum(){
    return 0
}
let formStepNum = _resetFormStepNum()
formSteps[formStepNum].classList.add('active')
_$$('.progress_step')[0].classList.add('active')

/* ================================= */

/* ==== TRANSITION SHOW SY HIDE === */
// Mampiseho ny card voalohany
_$$('a[href="#login"]').forEach((loginBtn) => {
    loginBtn.addEventListener('click', (e) => {
        // e.preventDefault()
        login = true
        register = false
        _$('.background_popup').style.display = 'flex'
        _$('.log_reg_wrap').style.setProperty('--wrapX', `${(logWidth + window.innerWidth) / 4}px`)
        _$('.login').classList.add('show1')
        _$('.register').style.opacity = '0'
    })
})

// Mampiseho ny card faharoa
_$('a[href="#register"]').addEventListener('click', (e) => {
    // e.preventDefault()
    login = false
    register = true
    _$('.background_popup').style.display = 'flex'
    _$('.log_reg_wrap').style.setProperty('--wrapX', `${(- logWidth - window.innerWidth) / 4}px`)
    _$('.register').classList.add('show1')
    _$('.login').style.opacity = '0'
    _goToFormStep(0, false)
})

// Manala ny card rehetra sy réinitialisation ny système
_$('.exit').addEventListener('click', () => {
    login = register = false
    _$('.login').style.animation = 'hide1 0.5s forwards' 
    _$('.register').style.animation = 'hide1 0.5s forwards'
    setTimeout(() => {
        _$('.background_popup').style.display = 'none'
        _$('.login').classList.remove('show1')
        _$('.login').classList.remove('hide2')
        _$('.login').style.animation = ''
        _$('.login').style.opacity = ''
        _$('.register').classList.remove('show1')
        _$('.register').classList.remove('hide2')
        _$('.register').style.animation = ''
        _$('.register').style.opacity = ''
        _$('.log_reg_wrap').style.transform = ''
        _$('.log_reg_wrap').style.transition = '0s'
    }, 500);
    setTimeout(() => {
        _resetFormStep()
    }, 500);
})

// Rehefa miseho ny card voalohany
// mampiseho ny card faharoa dia manala ny voalohany (slide effect) 
_$('.login a[href="#register"]').addEventListener('click', (e) => {
    // e.preventDefault()
    login = false
    register = true
    _$('.register').style.opacity = '1'
    _$('.login').classList.remove('show1')
    _$('.register').classList.remove('show1')
    _$('.register').classList.remove('hide2')
    _$('.log_reg_wrap').style.transition = `transform 0.5s`
    _$('.log_reg_wrap').style.transform = `translateX( ${(-logWidth - window.innerWidth) / 4}px )`
    _$('.login').classList.add('hide2')
    _goToFormStep(0, false)
})

// Rehefa miseho ny card faharoa
// mampiseho ny card voalohany dia manala ny faharoa (slide effect)
_$('.register a[href="#login"]').addEventListener('click', (e) => {
    // e.preventDefault()
    login = true
    register = false
    _$('.login').style.opacity = '1'
    _$('.login').classList.remove('show1')
    _$('.register').classList.remove('show1')
    _$('.login').classList.remove('hide2')
    _$('.log_reg_wrap').style.transition = `transform 0.5s`
    _$('.log_reg_wrap').style.transform = `translateX( ${(logWidth + window.innerWidth) / 4}px )`
    _$('.register').classList.add('hide2')
    setTimeout(() => {
        _resetFormStep()
    }, 500);
})

// responsive
window.addEventListener('resize', () => {
    gap = ((window.innerWidth - logWidth) / 2)
    _$('.log_reg_wrap').style.gap = `${gap}px`
    logWidth = 500//(4/10*window.innerWidth)
    _$('.login').style.setProperty('--width', `${logWidth}px`)
    _$('.register').style.setProperty('--width', `${logWidth}px`)
    _$('.log_reg_wrap').style.transition = '0s'
    if(login){
        _$('.log_reg_wrap').style.transform = `translateX(${(logWidth + window.innerWidth) / 4}px)`
    } else if(register) {
        _$('.log_reg_wrap').style.transform = `translateX(${(-logWidth - window.innerWidth) / 4}px)`
    }

})


_$$('.btn').forEach(btn => {
    btn.addEventListener('click', () => {
        if(btn.parentNode.classList.contains('btn_container')) {
            btn.style.transform = 'scale(0.8)'
        } else {
            btn.style.transform = 'scale(0.98)'
        }
        setTimeout(() => {
            btn.style.transform = 'scale(1)'
        }, 100);
    })
})
/* ============================== */


/* ==== REGISTRATION STEP ==== */

_$$('.btn-next').forEach(btnNext => {
    btnNext.addEventListener('click', (e) => {
        e.preventDefault()
        formStepNum++
        _goToFormStep(formStepNum)
        updateFormSteps()
        uptdateProgressBar()
    })
}) 
_$$('.btn-prev').forEach(btnPrev => {
    btnPrev.addEventListener('click', (e) => {
        e.preventDefault()
        formStepNum--
        _goToFormStep(formStepNum)
        updateFormSteps()
        uptdateProgressBar()
    })
})

function _resetFormStep() {
    formStepNum = _resetFormStepNum()
    formSteps.forEach(formStep => {
        formStep.classList.remove('active')
        formStep.classList.remove('inactive')
    })
    formSteps[formStepNum].classList.add('active')
    _goToFormStep(formStepNum)
    _$$('.progress_step').forEach((progressStep, index) => {
        if(index !== 0){
            progressStep.classList.remove('active')
        }
    })
    _$('.progress').style.transform = `scaleX(1)`
}
/**
 * 
 * @param {Number} index
 * @param {Boolean} transition
 */
function _goToFormStep(index, transition = true) {
    let posFormStep = _$('.register form').clientWidth / 3
    _$('.register form').style.transition = (transition)?`transform 0.5s`:`transform 0s`
    _$('.register form').style.transform = `translateX(${(-index +1) * posFormStep}px)` 
}
function updateFormSteps() {
    formSteps.forEach(formStep => {
        formStep.classList.contains('active')&&(      // if(formStep.classList.contains('active')){
            formStep.classList.remove('active') &     //     formStep.classList.add('inactive')
            formStep.classList.add('inactive')        //     formStep.classList.remove('active')
        )                                             // }             
    })
    formSteps[formStepNum].classList.add('active')
    formSteps[formStepNum].classList.remove('inactive')
}
function uptdateProgressBar() {
    _$$('.progress_step').forEach((progressStep, index) => {
            if(index < formStepNum +1){
                setTimeout(() => {
                    progressStep.classList.add('active')
                }, 350);
            } else {
                progressStep.classList.remove('active')
            }
        
    })
    let scaleValue = 1-(formStepNum/2)
    console.log(scaleValue);
    _$('.progress').style.transform = `scaleX(${scaleValue})`
}

// document.addEventListener('mouseover', (e) => {
//     console.log(e.target);
// })