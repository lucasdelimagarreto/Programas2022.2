const panels = document.querySelectorAll('.panel')

panels.forEach(panel => {
    panel.addEventListener('click', () => {
        removeerActiveClasse()
        panel.classList.add('active')
    })
})