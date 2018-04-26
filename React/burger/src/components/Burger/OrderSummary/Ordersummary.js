import React from 'react';
import Aux from '../../../hoc/Wrapper'
import Button from '../../UI/Button/Button'

const orderSummary = (props) => {
    const ingredientSummary = Object.keys(props.ingredients)
        .map(igKey => {
            return (
                <div key={igKey}>
                    <span style={{textTransform: 'capitalize'}}>{igKey}</span>: {props.ingredients[igKey]}
                </div>
        )})
    return (
        <Aux>
            <h3>Your order</h3>
            <p>Your Ingredients</p>
            <ul>
                {ingredientSummary}
            </ul>
            <p>Total: {props.price}</p>
            <p>Continue Checkout?</p>
            <Button clicked={props.purchaseCanceled} btnType="Danger">CANCEL</Button>
            <Button clicked={props.purchaseContinue} btnType="Success">CONTINUE</Button>
        </Aux>
    )
}

export default orderSummary;