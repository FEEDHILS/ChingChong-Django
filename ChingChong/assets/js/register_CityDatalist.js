const textInput = document.querySelector('input[name=city]')
const dataList = document.querySelector('datalist[id=Cities]')
let timeout;

// Запрос на сервер для получения JSON с первыми пяти похожими городами
async function DataBaseRequest() {
    const query = textInput.value;
    if (query != '') {
        const url = 'http://' + location.host + '/api/search_city?city=' + query
        const response = await fetch(url)
        const data = await response.json()
        dataList.innerHTML = '' // Удаляем все предыдущие опции
        // Добавляем новые опции
        data.results.forEach(item => {
            console.log(item.adress)
            const option = document.createElement('option');
            option.value = item.adress;
            dataList.appendChild(option)
        })
    }
}


function callback(evt) {
    clearTimeout(timeout)
    timeout = setTimeout(function(){
        DataBaseRequest()
    }, 200);
  }

textInput.addEventListener('input', callback)