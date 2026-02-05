document.addEventListener('DOMContentLoaded', () => {
  const bgInput = document.querySelector('#id_bg_color')
  const textInput = document.querySelector('#id_text_color')
  const preview = document.querySelector('#color-preview')

  const updatePreview = () => {
    if (!preview) return

    const bg = bgInput.value
    const text = textInput.value

    preview.style.backgroundColor = bg
    preview.style.color = text
  }

  if (bgInput) bgInput.addEventListener('input', updatePreview)
  if (textInput) textInput.addEventListener('input', updatePreview)
})
