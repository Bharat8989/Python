import { useRef } from "react";

export default function FocusInput() {
  const inputRef = useRef();

  function handleClick() {
    inputRef.current.focus();
  }

  return (
    <>
      <title>Ref Example</title>
      {/* <meta name="description" content="Understanding the ref prop" /> */}

      <input ref={inputRef} placeholder="Click the button to focus me" />

      <button onClick={handleClick}>Focus Input</button>
    </>
  );
}