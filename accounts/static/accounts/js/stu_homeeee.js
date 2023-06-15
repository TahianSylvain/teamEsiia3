


$(document).ready(() => {

    console.log("zzzzzzzzzzzz")

    course_list_container = document.querySelector('.course_list')

    const sendData = (dat) => {
        $.ajax({
            type: "GET",
            url: "",
            data: {
                'data': dat
            },
            success: (data_res) => {

                const courses = data_res.data_res
                document.querySelector('.subject_title').innerHTML = dat // subject_title
                course_list_container.innerHTML = '' // initialisation

                courses.forEach(course => {
                    let label = _createElementWithClass('span', 'col col1')
                    label.innerHTML = course.title
                    let date = _createElementWithClass('span', 'col col2')
                    date.innerHTML = course.date_upload
                    let hour = _createElementWithClass('span', 'col col3')
                    hour.innerHTML = course.hour_upload
                    let presence = _createElementWithClass('span', 'col col4')
                    if (course.present) {
                        presence.innerHTML = `<i class="ri-check-double-line present"></i>`
                    } else {
                        presence.innerHTML = `<i class="ri-close-line absent"></i>`
                    }
                    
                    // console.log(date);
                    
                    let row = _createElementWithClass('a', 'course row')
                    row.setAttribute('href', course.url_detail)
                    row.appendChild(label)
                    row.appendChild(date)
                    row.appendChild(hour)
                    row.appendChild(presence)
                    course_list_container.appendChild(row)
                });
            },
            error: (err) => {
                console.log(err);
            }
        })
    }

    $(".sbj_btn").click((e) => {
        e.preventDefault()
        console.log(e.target);
        sendData(e.target.id)
    })

    new Carousel(document.querySelector('.new_course_slide'), {
        slidesToScroll: 1,
        slidesToShow: 3,
        automatic: true,
    })

    // document.addEventListener('click', e => {
    //     console.log(e.target);
    // })

})