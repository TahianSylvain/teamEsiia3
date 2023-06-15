
/* --- initialisation registration step --- */
const formSteps = _$$('.form_step')
function _resetFormStepNum(){
    return 0
}
let formStepNum = _resetFormStepNum()
formSteps[formStepNum].classList.add('active')
_$$('.progress_step')[0].classList.add('active')
_goToFormStep(0, false)

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
    let posFormStep = _$('.register form').clientWidth / 4
    _$('.register form').style.transition = (transition)?`transform 0.5s`:`transform 0s`
    _$('.register form').style.transform = `translateX(${(-index +1) * posFormStep +195}px)` 
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
    let scaleValue = 1-(formStepNum/3)
    console.log(scaleValue);
    _$('.progress').style.transform = `scaleX(${scaleValue})`
}

// document.addEventListener('keyup', e => {
//     if(e.key == "Enter") {
//         if
//     }
// })

/* ============================================= */

