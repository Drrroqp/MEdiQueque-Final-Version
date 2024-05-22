// Модальное окно выбора врача 1

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-1").addEventListener("click", function() {
    document.getElementById("my-modal-1").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-1").addEventListener("click", function() {
    document.getElementById("my-modal-1").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-1").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-1 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-1").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

// Модальное окно выбора врача 2

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-2").addEventListener("click", function() {
    document.getElementById("my-modal-2").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-2").addEventListener("click", function() {
    document.getElementById("my-modal-2").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-2").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-2 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-2").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

// Модальное окно выбора врача 3

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-3").addEventListener("click", function() {
    document.getElementById("my-modal-3").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-3").addEventListener("click", function() {
    document.getElementById("my-modal-3").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-3").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-3 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-3").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

// Модальное окно выбора врача 4

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-4").addEventListener("click", function() {
    document.getElementById("my-modal-4").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-4").addEventListener("click", function() {
    document.getElementById("my-modal-4").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-4").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-4 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-4").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

// Модальное окно выбора врача 5

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-5").addEventListener("click", function() {
    document.getElementById("my-modal-5").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-5").addEventListener("click", function() {
    document.getElementById("my-modal-5").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-5").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-5 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-5").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

// Модальное окно выбора врача 6

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-6").addEventListener("click", function() {
    document.getElementById("my-modal-6").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-6").addEventListener("click", function() {
    document.getElementById("my-modal-6").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-6").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-6 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-6").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

// Модальное окно выбора врача 7

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-7").addEventListener("click", function() {
    document.getElementById("my-modal-7").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-7").addEventListener("click", function() {
    document.getElementById("my-modal-7").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-7").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-7 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-7").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

// Модальное окно выбора врача 8

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-8").addEventListener("click", function() {
    document.getElementById("my-modal-8").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-8").addEventListener("click", function() {
    document.getElementById("my-modal-8").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-8").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-8 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-8").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

// Модальное окно выбора врача 9

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-9").addEventListener("click", function() {
    document.getElementById("my-modal-9").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-9").addEventListener("click", function() {
    document.getElementById("my-modal-9").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-9").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-9 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-9").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

// Модальное окно выбора врача 10

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-10").addEventListener("click", function() {
    document.getElementById("my-modal-10").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-10").addEventListener("click", function() {
    document.getElementById("my-modal-10").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-10").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-10 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-10").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

// Модальное окно выбора врача 11

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-11").addEventListener("click", function() {
    document.getElementById("my-modal-11").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-11").addEventListener("click", function() {
    document.getElementById("my-modal-11").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-11").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-11 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-11").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

// Модальное окно выбора врача 12

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-12").addEventListener("click", function() {
    document.getElementById("my-modal-12").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-12").addEventListener("click", function() {
    document.getElementById("my-modal-12").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-12").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-12 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-12").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

document.addEventListener("DOMContentLoaded", function() {
  // Открыть модальное окно
  document.getElementById("open-modal-13").addEventListener("click", function() {
    document.getElementById("my-modal-13").classList.add("open");
  });

  // Закрыть модальное окно
  document.getElementById("close-my-modal-btn-13").addEventListener("click", function() {
    document.getElementById("my-modal-13").classList.remove("open");
  });

  // Закрыть модальное окно при нажатии на Esc
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      document.getElementById("my-modal-13").classList.remove("open");
    }
  });

  // Закрыть модальное окно при клике вне его
  document.querySelector("#my-modal-13 .modal__box").addEventListener('click', event => {
    event._isClickWithinModal = true;
  });

  document.getElementById("my-modal-13").addEventListener('click', event => {
    if (event._isClickWithinModal) {
      return;
    }
    event.currentTarget.classList.remove('open');
  });
});

  document.addEventListener("DOMContentLoaded", function() {
    const anchors = document.querySelectorAll('a[href*="#"]');
    
    for (let anchor of anchors) {
      anchor.addEventListener("click", function(event) {
        event.preventDefault();
        const blockID = anchor.getAttribute('href');
        const targetElement = document.querySelector(blockID);
        const topOffset = targetElement.getBoundingClientRect().top + window.pageYOffset; // Учитываем отступы и текущую позицию прокрутки
        window.scrollTo({
          top: topOffset,
          behavior: "smooth"
        });
      });
    }
  });
