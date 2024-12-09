import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
`;

export const Form = styled.form`
  display: flex;
  flex-direction: column;
  justify-content: stretch;
  align-items: flex-start;
  gap: 12px;
  width: 100%;
`;

export const ErrorMessage = styled.p`
  margin: 0;
  color: #F93C65;
  font-family: Actay Wide;
  font-size: 12px;
  font-weight: 700;
  line-height: 1.26;
`;
