import React, { createContext, useContext, useReducer } from 'react'

const CardStateContext = createContext();
const CardDispatchContext = createContext();

const reducer = (state, action) => {
    switch(action.type) {
        case "ADD":
            return [...state, {id: action.id, name: action.name, qty: action.qty,
                                size: action.size, price: action.price, img: action.img}]

        default:
            console.log("Error in Reducer")
    }
}

export const CartProvider = ({children}) => {
    const [state, dispatch] = useReducer(reducer, [])
    return (
        <CardDispatchContext.Provider value={dispatch}>
            <CardStateContext.Provider value={state}>
                {children}
            </CardStateContext.Provider>
        </CardDispatchContext.Provider>
    );
}

export const useCart = () => useContext(CardStateContext);
export const useDispatchCart = () => useContext(CardDispatchContext)