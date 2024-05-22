// Модальное окно выбора врача для записи

document.addEventListener("DOMContentLoaded", function() {
    // Открыть модальное окно
    document.getElementById("open-modal-btn").addEventListener("click", function() {
      document.getElementById("my-modal").classList.add("open");
    });
  
    // Закрыть модальное окно
    document.getElementById("close-my-modal-btn").addEventListener("click", function() {
      document.getElementById("my-modal").classList.remove("open");
    });
  
    // Закрыть модальное окно при нажатии на Esc
    window.addEventListener('keydown', (e) => {
      if (e.key === "Escape") {
        document.getElementById("my-modal").classList.remove("open");
      }
    });
  
    // Закрыть модальное окно при клике вне его
    document.querySelector("#my-modal .modal__box").addEventListener('click', event => {
      event._isClickWithinModal = true;
    });
  
    document.getElementById("my-modal").addEventListener('click', event => {
      if (event._isClickWithinModal) {
        return;
      }
      event.currentTarget.classList.remove('open');
    });
  });

// Модальные окна авторизации и регистрации

  document.addEventListener("DOMContentLoaded", function() {
    // Открыть модальное окно
    document.getElementById("open-modal-btn-registration").addEventListener("click", function() {
      document.getElementById("my-modal-registr").classList.add("open");
    });
    document.getElementById("open-modal-btn-registration2").addEventListener("click", function() {
      document.getElementById("my-modal-registr").classList.add("open");
    });
    document.getElementById("open-modal-btn-registration3").addEventListener("click", function() {
      document.getElementById("my-modal-autorization").classList.remove("open");
      document.getElementById("my-modal-registr").classList.add("open");
    });
  
    // Закрыть модальное окно
    document.getElementById("close-my-modal-btn-reg").addEventListener("click", function() {
      document.getElementById("my-modal-registr").classList.remove("open");
    });
  
    // Закрыть модальное окно при нажатии на Esc
    window.addEventListener('keydown', (e) => {
      if (e.key === "Escape") {
        document.getElementById("my-modal-registr").classList.remove("open");
      }
    });
  
    // Закрыть модальное окно при клике вне его
    document.querySelector("#my-modal-registr .modal__box").addEventListener('click', event => {
      event._isClickWithinModal = true;
    });
  
    document.getElementById("my-modal-registr").addEventListener('click', event => {
      if (event._isClickWithinModal) {
        return;
      }
      event.currentTarget.classList.remove('open');
    });
  });

  document.addEventListener("DOMContentLoaded", function() {
    // Открыть модальное окно
    document.getElementById("open-modal-btn-login").addEventListener("click", function() {
      document.getElementById("my-modal-autorization").classList.add("open");
    });
    document.getElementById("open-modal-btn-login2").addEventListener("click", function() {
      document.getElementById("my-modal-autorization").classList.add("open");
    });
  
    // Закрыть модальное окно
    document.getElementById("close-my-modal-btn-aut").addEventListener("click", function() {
      document.getElementById("my-modal-autorization").classList.remove("open");
    });
  
    // Закрыть модальное окно при нажатии на Esc
    window.addEventListener('keydown', (e) => {
      if (e.key === "Escape") {
        document.getElementById("my-modal-autorization").classList.remove("open");
      }
    });
  
    // Закрыть модальное окно при клике вне его
    document.querySelector("#my-modal-autorization .modal__box").addEventListener('click', event => {
      event._isClickWithinModal = true;
    });
  
    document.getElementById("my-modal-autorization").addEventListener('click', event => {
      if (event._isClickWithinModal) {
        return;
      }
      event.currentTarget.classList.remove('open');
    });
  });