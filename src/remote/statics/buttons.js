const handleClick = (el) => {
    const key = el.target.value;
    fetch(`/p/${key}`, {
        'method': 'POST',
        // 'body': {
        //     'key': key,
        // }
    }).then(r => console.log(r)).catch(e => console.error(e));
}

document.querySelectorAll('.key').forEach(e => e.addEventListener('click', handleClick))