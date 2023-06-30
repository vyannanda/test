/// <reference types="cypress" />

describe('example to-do app', () => {
    beforeEach(() => {
      cy.visit('https://www.saucedemo.com')
    })
  
    it('log in', () => {
      //cy.visit('https://www.saucedemo.com/')
      cy.get('#user-name').type('standard_user')
      cy.get('#password').type('secret_sauce')
      cy.get('#login-button').click()
    })

   it('make a purchase', () => {
      cy.get('#add-to-cart-sauce-labs-backpack').click()
      cy.get('#shopping_cart_container').click()
      cy.get('#checkout').click()
      cy.get('#first-name').type('Mawar')
      cy.get('#last-name').type('Budiman')
      cy.get('#postal-code').type('40535')
      cy.get('#continue').click()
      cy.get('#finish').click()
    })
})