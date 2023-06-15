console.log('tea_homeiiiiiiii');

let subject_clicked = '',
    input_file = document.querySelector('#course_video'),
    result_file = document.querySelector('.result_file')


$('.dept').click(e => {
    e.preventDefault()
    console.log(e.target.id);
    showSubject(e.target.id)
})

const showSubject = (dat) => {

    // console.log(dat);
    document.querySelectorAll(`.subjects_container`).forEach(el => {
        el.style.paddingTop = '0px'     // RESET
    })
    document.querySelectorAll('.subjects').forEach(element => {
        element.innerHTML = '' // RESET
    })

    $.ajax({
        type: 'GET',
        url: '',
        data: {
            'data': dat,
        },
        success: (res) => {
            res.subject_res.forEach(data => {
                let sbj = _createElementWithClass('li', 'subject')
                // console.log(sbj);
                sbj.innerHTML = data.subject_name
                document.querySelector(`.${dat}`).appendChild(sbj)
                document.querySelector(`.${dat}_container`).style.paddingTop = '10px'
            });
        }
    })

}


document.addEventListener('click', e => {
    console.log(e.target);
    
    // SHOW COURSES
    if(e.target.classList.contains('subject')) {
        showCourse(e.target.innerText)
    }
    else {
        document.querySelectorAll(`.subjects_container`).forEach(el => {
            el.style.paddingTop = '0px'
        })
        document.querySelectorAll('.subjects').forEach(element => {
            element.innerHTML = ''
        })

        // CREATE COURSE MODAL
        if(e.target.id == 'add_course') {
            document.querySelector('.create_course_wrap').style.display = "block"
            // document.querySelector('input#course_subject').value = subject_clicked
            
            $.ajax({
                type: 'GET',
                url: '',
                data: {
                    'subject_add_course': subject_clicked,
                },
                success: (res) => {
                    console.log(res);
                },
                error: (err) => {
                    console.log(err);
                }
            })

        }
    }
})

const showCourse = (dat) => {

    subject_clicked = dat  // utile à la creation d'un cours (course.subject)

    document.querySelector('.course_list').innerHTML = '' // RESET: efface ce qui est déjà là

    try {
        document.querySelector('button.add_course').remove() // ------||------
    } catch (err) {
        console.log(err);
    }

    $.ajax({
        type: 'GET',
        url: '',
        data: {
            'sbj': dat,
        },
        success: (res) => {
            const courses = res.courses_res
            console.log(res.courses_res);
            document.querySelector('.course_header span').innerHTML = `${dat} in ${res.dept}`
            let btn = _createElementWithClass('button', 'add_course')
            btn.setAttribute('id', 'add_course')
            btn.innerHTML = `Add Course <i class="ri-add-line" id="add_course"></i>`
            document.querySelector('.course_header').appendChild(btn)
            courses.forEach(course => {
                console.log(course.title);
                let label = _createElementWithClass('span', 'col col1')
                label.innerHTML = course.title
                let date = _createElementWithClass('span', 'col col2')
                date.innerHTML = course.date
                let hour = _createElementWithClass('span', 'col col3')
                hour.innerHTML = course.hour
                
                let row = _createElementWithClass('a', 'row')
                row.setAttribute('href', course.url)
                row.style.textDecoration = 'none'
                row.appendChild(label)
                row.appendChild(date)
                row.appendChild(hour)
                document.querySelector('.course_list').appendChild(row)
            })
        }
    })

}


// creation course
input_file.addEventListener('change', e => {
    console.log(input_file.files[0]);
    result_file.innerHTML = input_file.files[0].name
})
document.querySelector('#btn_close').addEventListener('click', e => {
    document.querySelector('.create_course_wrap').style.display = "none"
})